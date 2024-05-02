from rest_framework import serializers
from market.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'stock']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UpdateProductStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['stock']
        read_only_fields = ['name', 'price', 'category', 'image']