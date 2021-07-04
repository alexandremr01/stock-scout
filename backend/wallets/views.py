from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from django.db import connection

from .serializers import WalletSerializer, OperationSerializer
from .models import Wallet, Operations
from users.models import Profile
from rest_framework.response import Response
import json


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all().order_by('name')
    serializer_class = WalletSerializer

    def list(self, request):
        user = request.user
        profile = Profile.objects.filter(user = user).first()
        queryset = Wallet.objects.filter(profile = profile)
        serializer = WalletSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        user = request.user
        profile = Profile.objects.filter(user=user).first()
        queryset = Wallet.objects.filter(profile=profile)
        rows = []
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT symbol, 
                   SUM(CASE WHEN type = 'buy' THEN quantity ELSE -quantity END) quantity,
                   SUM(CASE WHEN type = 'buy' THEN value END) paid_value,
                   SUM(CASE WHEN type = 'buy' THEN quantity END) total_bought
            FROM wallets_operations 
            WHERE wallet_id = %s 
            GROUP BY symbol""", [pk])
            rows = cursor.fetchall()
        serializer = WalletSerializer(queryset, many=True)
        resp = []
        print(rows)
        for r in rows:
            if r[3] == 0 or r[3] is None:
                avg = 0
            else:
                avg = r[2]/r[3]
            resp.append({'symbol': r[0], 'quantity': r[1], 'avg_value': avg})
        return JsonResponse({'stocks': resp})

    def create(self, request, pk=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user = request.user
        profile = Profile.objects.filter(user = user).first()
        wallet = Wallet(profile=profile, name=body['name'])
        wallet.save()
        return Response(WalletSerializer(wallet).data)


class OperationsViewSet(viewsets.ModelViewSet):
    queryset = Operations.objects.all().order_by('day')
    serializer_class = OperationSerializer

    def list(self, request, pk):
        wallet = Wallet.objects.filter(id=pk).first()
        print(wallet.name)
        queryset = Operations.objects.filter(wallet=wallet)
        serializer = OperationSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, pk):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        wallet = Wallet.objects.filter(id=pk).first()
        sim = Operations(wallet=wallet, day=body['day'], type=body['type'],
                         quantity=body['quantity'], value=body['value'], symbol=body['symbol'])
        sim.save()
        return Response(OperationSerializer(sim).data)

    def destroy(self, request, pk_wallet, pk_op):
        Operations.objects.filter(id=pk_op).delete()
        return HttpResponse(status=200)


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
