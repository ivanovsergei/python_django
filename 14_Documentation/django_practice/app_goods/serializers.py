from rest_framework import serializers
from .models import Good


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(allow_blank=True)
    weight = serializers.FloatField(min_value=0)


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ['id', 'name', 'description', 'weight']
