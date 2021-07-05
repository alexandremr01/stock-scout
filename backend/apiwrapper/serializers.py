import json

from rest_framework import serializers
from .models import StockTimeSeries, CoinQuotation
from .api_client import alpha_vantage_client

from datetime import datetime, timedelta, timezone

class CoinQuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinQuotation
        fields = ['buy', 'sell', 'variation']

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
    
    return time_series.data

# json to map
def get_daily_history(symbol):
    data = get_or_update_stock_time_series(symbol, 'DAY')

    daily_hist = {}
    for daily_intel in eval(data):
        daily_hist[daily_intel['Date']] = daily_intel['close']
    return daily_hist

def get_pseudo_current_stock_value(symbols):
    values = {}

    for symbol in symbols:
        data = get_or_update_stock_time_series(symbol, 'DAY')
        first_record = eval(data)[0]['close']
        values[symbol] = first_record
    
    return values
