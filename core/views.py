from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ProductSerializer,ProductDetailSerializer,OrderSerializer,OrderProductSerializer
from .models import Product, ProductImage,Order,OrderedProduct


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.prefetch_related('image').all()