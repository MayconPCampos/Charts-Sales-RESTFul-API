from rest_framework import serializers
from .models import Sale


class SaleSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username") # inclui username de cada entrada na resposta
    class Meta:
        model = Sale
        fields = ["pk", "client", "product", "price", "date", "username"]
