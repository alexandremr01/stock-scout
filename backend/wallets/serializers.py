# serializers.py
from rest_framework import serializers
from .models import Wallet, Operations

class WalletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wallet
        fields = ('name', 'created_at', 'id')

class OperationSerializer(serializers.ModelSerializer):
    wallet_id = serializers.PrimaryKeyRelatedField(queryset=Wallet.objects.all())

    class Meta:
        model = Operations
        fields = ('id', 'wallet_id', 'value', 'type', 'symbol', 'quantity', 'day')

    def create(self, validated_data):
        op = Operations(**validated_data)
        op.save()
        return op
