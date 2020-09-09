"""Serializer Income model."""

from rest_framework import serializers
from .models import Expense


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expense
        fields = ('uuid', 'amount', 'category', 'description', 'created_at')
