
from django.urls import path
from .views import ProductListView, ProductDetailView, FeaturedProductList,AddToCart

urlpatterns = [
    path('products/', ProductListView.as_view(), name="product-list"),
    path('product-features/', FeaturedProductList.as_view(), name="product-features"),
    path('product-detail/<str:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('add-to-cart/', AddToCart.as_view(), name="add-to-cart"),

    
    



]
