from django.shortcuts import render
from .models import StockTimeSeries, CoinQuotation
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .api_client import hg_brasil_client
from .serializers import get_or_update_stock_time_series, CoinQuotationSerializer

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
        data = get_or_update_stock_time_series(symbol, freq)
        return Response(data)

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
