from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from django.http import JsonResponse

from .serializers import WalletSerializer
from .models import Wallet


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all().order_by('name')
    serializer_class = WalletSerializer


class PhraseView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        response = JsonResponse({
            'data': [
                'Deploy automático da main atualizado!',
                'And you get a phrase from the API!',
                'And you get a phrase from the API!',
                'And you get a phrase from the API!',
                'And you get a phrase from the API!',
            ]
        })
        return response
