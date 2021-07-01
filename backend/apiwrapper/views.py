from django.shortcuts import render
from .models import StockTimeSeries, CoinQuotation
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from datetime import datetime, timedelta, timezone

from .api_client import alpha_vantage_client, hg_brasil_client
from .serializers import alphav_to_ss, CoinQuotationSerializer

# Create your views here.
class StockDetail(APIView):
    """
    Retrieves a time series from a API
    given a set of query params
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        symbol = request.query_params.get('symbol')
        freq = request.query_params.get('freq')
        filter1 = StockTimeSeries.objects.filter(ticker=symbol)
        if filter1.exists():
            filter2 = filter1.filter(frequency=freq)
            if filter2.exists():
                time_series = filter2[0]
                refresh = {'DAY': 1, 'WEEK': 7, 'MONTH': 30}

                if datetime.now(timezone.utc) - time_series.last_modified < timedelta(days=refresh[freq]):
                    return Response(time_series.data)

                alphav_json = alpha_vantage_client(symbol, freq)
                ss_json = alphav_to_ss(alphav_json, freq)
                time_series.data = ss_json
                time_series.save()
                return Response(ss_json)

        alphav_json = alpha_vantage_client(symbol, freq)
        ss_json = alphav_to_ss(alphav_json, freq)
        new_time_series = StockTimeSeries(ticker=symbol, data=ss_json, frequency=freq)
        new_time_series.save()
        return Response(ss_json)

class CoinDetail(APIView):
    """
    Lists a pseudo real time value for a given coin
    (delay of between 15 minutes and 1 hour)
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        coin_name = request.query_params.get('code')
        filter = CoinQuotation.objects.filter(name=coin_name)
        if filter.exists():
            coin_quotation = filter[0]

            if datetime.now(timezone.utc) - coin_quotation.last_modified < timedelta(minutes=15):
                return Response(CoinQuotationSerializer(coin_quotation).data)
            
            hgbr_json = hg_brasil_client()
            data = hgbr_json["results"]["currencies"][coin_quotation.name]
            coin_quotation.buy = data["buy"]
            coin_quotation.sell = data["sell"]
            coin_quotation.variation = data["variation"]
            coin_quotation.save()
            return Response(CoinQuotationSerializer(coin_quotation).data)
        
        hgbr_json = hg_brasil_client()
        data = hgbr_json["results"]["currencies"][coin_name]
        new_coin_quotation = CoinQuotation(name=coin_name, buy=data["buy"], sell=data["sell"], variation=data["variation"])
        new_coin_quotation.save()
        return Response(CoinQuotationSerializer(new_coin_quotation).data)
