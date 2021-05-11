from django.shortcuts import render
from rest_framework import viewsets

from .serializers import WalletSerializer
from .models import Wallet


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all().order_by('name')
    serializer_class = WalletSerializer