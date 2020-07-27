"""Serializer Income model."""

from rest_framework import serializers
from .models import Income


class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Income
        fields = ('uuid', 'description', 'amount', 'created_at')
