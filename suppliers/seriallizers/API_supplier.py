from rest_framework import serializers
from suppliers.models import Supplier
from products.seriallizers.product import ProductSerializer


class SupplierAPISerializer(serializers.ModelSerializer):
    '''Сериализатор API сущности поставщика'''
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    product = ProductSerializer(many=True, required=False)

    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierAPICreateSerializer(serializers.ModelSerializer):
    '''Сериализатор (создания) API сущности поставщика'''

    class Meta:
        model = Supplier
        fields = '__all__'
