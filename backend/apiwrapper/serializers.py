import json

from rest_framework import serializers
from .models import CoinQuotation

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
