from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from django.db import connection
from apiwrapper.serializers import get_pseudo_current_stock_value, get_or_update_coin_quotations, get_daily_history
from .serializers import WalletSerializer, OperationSerializer
from .models import Wallet, Operations
from users.models import Profile
from rest_framework.response import Response
import json
from datetime import datetime


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
        if isAuthorized(request, pk) is False:
            return HttpResponse(status=403)
        rows = []
        currency = request.query_params.get('currency')
        if currency is None:
            currency = 'BRL'

        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT symbol, 
                   SUM(CASE WHEN type = 'buy' THEN quantity ELSE -quantity END) quantity,
                   SUM(CASE WHEN type = 'buy' THEN value*quantity END) paid_value,
                   SUM(CASE WHEN type = 'buy' THEN quantity END) total_bought
            FROM wallets_operations op
            JOIN wallets_wallet w ON w.id = op.wallet_id
            WHERE wallet_id = %s AND w.profile_id = %s 
            GROUP BY symbol""", [pk, profile.id])
            rows = cursor.fetchall()
        resp = []
        current_total_value = 0
        for r in rows:
            if r[3] == 0 or r[3] is None:
                avg = 0
            else:
                avg = r[2]/r[3]
            values = get_pseudo_current_stock_value([r[0]])
            str_value = values[r[0]]
            try:
                value = float(str_value)
            except ValueError:
                value = 0

            usd_value_s = get_or_update_coin_quotations('USD')
            try:
                usd_value = float(usd_value_s.sell)
            except ValueError:
                usd_value = 0

            if is_brl(r[0]) and currency == "USD":
                value = round(value/usd_value, 2)
            elif not is_brl(r[0]) and currency == "BRL":
                value = round(value*usd_value, 2)


            current_total_value += value*r[1]

            resp.append({'symbol': r[0], 'quantity': r[1], 'avg_value': round(avg, 2), 'current_unit': value, 'current_total': value*r[1]})
        return JsonResponse({'stocks': resp, 'current_total_value': current_total_value})

    def create(self, request, pk=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user = request.user
        profile = Profile.objects.filter(user = user).first()
        wallet = Wallet(profile=profile, name=body['name'])
        wallet.save()
        return Response(WalletSerializer(wallet).data)

    def history(self, request, pk):
        if isAuthorized(request, pk) is False:
            return HttpResponse(status=403)
        wallet = Wallet.objects.filter(id=pk).first()
        operations = Operations.objects.filter(wallet=wallet).order_by('day')

        symbols = []
        for op in operations:
            symbols.append(op.symbol)
        days, histories = get_daily_history(symbols)

        op_iter = 0
        obtained_symbols = {}
        wallet_history = []
        for day in days:
            while op_iter < len(operations) and operations[op_iter].day <= datetime.strptime(day, '%Y-%m-%d').date():
                op = operations[op_iter]
                if not op.symbol in obtained_symbols:
                    obtained_symbols[op.symbol] = 0
                if op.type == 'buy':
                    obtained_symbols[op.symbol] += op.quantity
                else:
                    obtained_symbols[op.symbol] -= op.quantity
                if obtained_symbols[op.symbol] == 0:
                    obtained_symbols.pop(op.symbol)
                op_iter += 1

            day_value = 0
            for symbol, quantity in obtained_symbols.items():
                if day in histories[symbol]:
                    day_value += quantity*float(histories[symbol][day])
            wallet_history.append({'day': day, 'value': str(round(day_value, 2))})
        decreasing_history = []
        original_len = len(wallet_history)
        for i in range(original_len):
            decreasing_history.append(wallet_history.pop())
        return Response(json.dumps(decreasing_history))


class OperationsViewSet(viewsets.ModelViewSet):
    queryset = Operations.objects.all().order_by('day')
    serializer_class = OperationSerializer

    def list(self, request, pk):
        if isAuthorized(request, pk) is False:
            return HttpResponse(status=403)
        wallet = Wallet.objects.filter(id=pk).first()
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
        if isAuthorized(request, pk_wallet) is False:
            return HttpResponse(status=403)
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

def isAuthorized(request, wallet_id):
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    walletQs = Wallet.objects.filter(id=wallet_id)
    if not walletQs:
        return False
    wallet = walletQs.first()
    return wallet.profile.id == profile.id

def is_brl(symbol):
    parts = symbol.split('.')
    if len(parts) < 2:
        return False
    return parts[1] == "SA"
