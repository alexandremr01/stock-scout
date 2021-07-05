import json

from rest_framework import serializers
from .models import StockTimeSeries, CoinQuotation, Index
from .api_client import alpha_vantage_client, hg_brasil_client

from datetime import datetime, timedelta, timezone

class CoinQuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinQuotation
        fields = ['buy', 'sell', 'variation']

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = ['selic', 'cdi', 'date', 'usd', 'eur', 'ibovespa', 'nasdaq', 'bitcoin']

# json to json
def alphav_to_ss(alphav_data, freq):
    alphav = {
        'DAY': 'Time Series (Daily)',
        'WEEK': 'Weekly Adjusted Time Series',
        'MONTH': 'Monthly Adjusted Time Series'
    }

    ss_arr = []
    time_series = alphav_data[alphav[freq]]
    for key, value in time_series.items():
        ss_dict = {
            'Date': key,
            'open': value['1. open'],
            'close': value['4. close'],
            'high': value['2. high'],
            'low': value['3. low']
        }
        ss_arr.append(ss_dict)
    
    return json.dumps(ss_arr)

# json to model
def get_or_update_stock_time_series(symbol, freq):
    query = StockTimeSeries.objects.filter(ticker=symbol).filter(frequency=freq)
    refresh = {'DAY': 1, 'WEEK': 7, 'MONTH': 30}
    time_series = None

    if query.exists():
        time_series = query[0]

    if not query.exists():
        alphav_json = alpha_vantage_client(symbol, freq)
        ss_json = alphav_to_ss(alphav_json, freq)
        new_time_series = StockTimeSeries(ticker=symbol, data=ss_json, frequency=freq)
        new_time_series.save()
        time_series = new_time_series
    
    if datetime.now(timezone.utc) - time_series.last_modified > timedelta(days=refresh[freq]):
        alphav_json = alpha_vantage_client(symbol, freq)
        ss_json = alphav_to_ss(alphav_json, freq)
        time_series.data = ss_json
        time_series.save()
    
    return time_series

def get_or_update_coin_quotations(currency):
    query = CoinQuotation.objects.filter(name=currency)
    coin_quotation = None

    if query.exists():
        coin_quotation = query[0]
    
    if not query.exists():
        hgbr_json = hg_brasil_client()
        data = hgbr_json["results"]["currencies"][currency]
        coin_quotation = CoinQuotation(name=currency, buy=data["buy"], sell=data["sell"], variation=data["variation"])
        coin_quotation.save()

    if datetime.now(timezone.utc) - coin_quotation.last_modified < timedelta(minutes=15):
        hgbr_json = hg_brasil_client()
        data = hgbr_json["results"]["currencies"][coin_quotation.name]
        coin_quotation.buy = data["buy"]
        coin_quotation.sell = data["sell"]
        coin_quotation.variation = data["variation"]
        coin_quotation.save()

    return coin_quotation

def get_or_update_taxes():
    query = Index.objects.filter(date=datetime.now().date())
    index = None

    if query.exists():
        index = query[0]

    if not query.exists() or datetime.now(timezone.utc) - index.last_modified < timedelta(hours=1):
        hgbr_json = hg_brasil_client()
        data_taxes = hgbr_json["results"]["taxes"][0]
        data_coins = hgbr_json["results"]["currencies"]
        data_stocks = hgbr_json["results"]["stocks"]
        print(hgbr_json["results"])
        index = Index(date=datetime.now().date(), cdi=data_taxes["cdi"], selic=data_taxes["selic"],
                      usd=data_coins["USD"]["sell"], eur=data_coins["EUR"]["sell"],
                      ibovespa=data_stocks["IBOVESPA"]["points"] , nasdaq=data_stocks["NASDAQ"]["points"],
                      bitcoin=data_coins["BTC"]["sell"])
        index.save()

    return index

# json to map
def get_daily_history(symbols):
    daily_histories = {}

    for symbol in symbols:
        time_series = get_or_update_stock_time_series(symbol, 'DAY')
        daily_hist = {}
        for daily_intel in eval(time_series.data):
            daily_hist[daily_intel['Date']] = daily_intel['close']
        daily_histories[symbol] = daily_hist

    time_series = get_or_update_stock_time_series('IBM', 'DAY')
    days = []
    for daily_intel in eval(time_series.data):
        days.append(daily_intel['Date'])
    increasing_days = []
    original_len = len(days)
    for i in range(original_len):
        increasing_days.append(days.pop())

    return increasing_days, daily_histories

def get_pseudo_current_stock_value(symbols):
    values = {}

    for symbol in symbols:
        time_series = get_or_update_stock_time_series(symbol, 'DAY')
        first_record = eval(time_series.data)[0]['close']
        values[symbol] = first_record
    
    return values
