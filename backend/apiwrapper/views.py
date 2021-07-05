from django.shortcuts import render
from .models import CoinQuotation
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import get_or_update_stock_time_series, get_or_update_coin_quotations, CoinQuotationSerializer, get_or_update_taxes, IndexSerializer
from django.http import JsonResponse

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
        time_series = get_or_update_stock_time_series(symbol, freq)
        return Response(time_series.data)

class CoinDetail(APIView):
    """
    Lists a pseudo real time value for a given coin
    (delay of between 15 minutes and 1 hour)
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        coin_name = request.query_params.get('code')
        coin_quotation = get_or_update_coin_quotations(coin_name)
        return Response(CoinQuotationSerializer(coin_quotation).data)

class IndexesDetail(APIView):
    """
    Lists a pseudo real time value for a given coin
    (delay of between 15 minutes and 1 hour)
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        index = get_or_update_taxes()
        usd = get_or_update_coin_quotations('USD')
        eur = get_or_update_coin_quotations('EUR')
        btc = get_or_update_coin_quotations('BTC')
        return JsonResponse(
            {
                'indexes': IndexSerializer(index).data,
                'usd': CoinQuotationSerializer(usd).data,
                'eur':CoinQuotationSerializer(eur).data,
                'btc': CoinQuotationSerializer(btc).data,
             }
        )
