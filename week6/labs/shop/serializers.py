from rest_framework import serializers
from shop.models import Category, Product
from auth_.serializers import MyUserSerializer


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_by = MyUserSerializer(required=False)
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'created_by', 'created_at')


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.IntegerField(required=True)
    category = CategorySerializer(required=False)


    class Meta:
        model = Product
        fields = ('id', 'name', 'status', 'category')