from rest_framework import serializers
from product.models import Category
from product.models import Product
from product.models import Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']









class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'









class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'