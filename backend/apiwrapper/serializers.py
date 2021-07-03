import json

from rest_framework import serializers
from .models import StockTimeSeries, CoinQuotation
from .api_client import alpha_vantage_client

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

# json to map
def get_daily_history(symbol):
    time_series = None
    query = StockTimeSeries.objects.filter(ticker=symbol).filter(frequency='DAY')

    if query.exists():
        time_series = query[0]
    else:
        time_series = query[0]
        alphav_json = alpha_vantage_client(symbol, 'DAY')
        ss_json = alphav_to_ss(alphav_json, 'DAY')
        new_time_series = StockTimeSeries(ticker=symbol, data=ss_json, frequency='DAY')
        new_time_series.save()
        time_series = new_time_series

    daily_hist = {}
    for daily_intel in eval(time_series.data):
        daily_hist[daily_intel['Date']] = daily_intel['close']
    return daily_hist
