from shop.models import Category, Product

from shop.serializers import CategorySerializer, ProductSerializer
import json
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, viewsets, generics
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

class CategoryViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Category.objects.for_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CategoryProductsAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        try:
            category = Category.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except Category.DoesNotExist:
            raise Http404
        return category.products.all()

    def perform_create(self, serializer):
        try:
            category = Category.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except Category.DoesNotExist:
            raise Http404
        serializer.save(category=category)


class ProductViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()