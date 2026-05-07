from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Transaction
        fields = [
            'id',
            'amount',
            'type',
            'category',
            'date',
            'description',
        ]