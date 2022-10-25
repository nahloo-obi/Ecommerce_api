from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ProductSerializer,ProductDetailSerializer,OrderSerializer,OrderProductSerializer
from .models import Product, ProductImage,Order,OrderedProduct
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils import timezone




class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.prefetch_related('image').all()
    
class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.prefetch_related('image').all()
    
class FeaturedProductList(ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        product = Product.objects.prefetch_related("image").filter(is_featured=True)
        return product
    
class AddToCart(APIView):

    def post(self,request):
        id = request.data.get("id", None)
        size = request.data.get('size', None)
        colour = request.data.get('colour', None)
        quantities = request.data.get('product-quantity', None)
        quantity = int(quantities)
        
        product = Product.objects.get(id=id)
            
        ordered_product, created = OrderedProduct.objects.get_or_create(
            product = product,
            user=request.user,
            ordered=False,
            colour = colour,
            size = size
        )
        
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if order.products.filter(product__id=product.id, colour=colour, size=size).exists():
                ordered_product.quantity += int(quantity)
                ordered_product.save()
                return Response(status=status.HTTP_201_CREATED)
                
            else: 
                ordered_product.quantity = quantity
                ordered_product.save()
                order.products.add(ordered_product)
                return Response(status=status.HTTP_201_CREATED)
        else:
            ordered_date = timezone.now()
            ordered_product.quantity = quantity
            ordered_product.save()
            order = Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.products.add(ordered_product)
            return Response(status=status.HTTP_201_CREATED)
        
    