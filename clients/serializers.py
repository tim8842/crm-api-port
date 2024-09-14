from rest_framework import serializers
from .models import Client, Deal


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    deals = DealSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = "__all__"
