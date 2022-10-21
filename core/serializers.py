from dataclasses import fields
from rest_framework import serializers
from core.models import Address, Product, Order, OrderedProduct, Payment, ProductImage, ProductReview
from django_countries.serializer_fields import CountryField

class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value

class ProductImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImage
        fields = ["image"]

class ProductSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    sale_type = serializers.SerializerMethodField()
    accessory_type = serializers.SerializerMethodField()
    colour = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    image = ProductImageSerializer(read_only=True, many=True)
    
    class Meta:
        model = Product
        fields = ['id','name', 'price', 'description', 'gender',  'sale_type', 'accessory_type',  'colour',  'size', 'is_featured', 'image']
        
    def get_gender(self, obj):
        return obj.get_gender_display()
    
    def get_sale_type(self, obj):
        return obj.get_sale_type_display()
    def get_accessory_type(self, obj):
        return obj.get_accessory_type_display()
    def get_colour(self, obj):
        return obj.get_colour_display()
    def get_size(self, obj):
        return obj.get_size_display()
    
  
    


    
    
class OrderProductSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()
    
    class Meta:
        model = OrderedProduct
        fields = ['id', 'product', 'quantity', 'final_price', ]
        
    def get_item(self, obj):
        return ProductSerializer(obj.item).data
        
    def get_final_price(self, obj):
        return obj.get_final_price()
    
    
    
   
class OrderSerializer(serializers.ModelSerializer):
    order_products = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    coupon = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['id', 'order_products', 'total',]
        
    def get_order_products(self, obj):
        return OrderProductSerializer(obj.items.all(), many = True).data
    
    def get_total(self,obj):
        return obj.get_total()
   


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id','title', 'price', 'category',  'description',]
        
    def get_category(self, obj):
        return obj.get_category_display()
    
    def get_label(self, obj):
        return obj.get_label_display()
    
    
    

class AddressSerializer(serializers.ModelSerializer):
    country = CountryField()
    
    class Meta:
        model = Address
        fields = ['user','id','street_address', 'apartment_address','country', 'zip' ]
   
class PaymentSerializer(serializers.Serializer):
    class Meta:
        model = Payment
        fields =['id', 'amount', 'timestamp']