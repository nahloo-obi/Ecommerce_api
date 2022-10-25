
from django.urls import path
from .views import (ProductListView, ProductDetailView,
                    FeaturedProductList,AddToCart,
                    OrderSummaryPage, AddSingleQuantityToProduct,RemoveSingleQuantityFromProduct,Address)

urlpatterns = [
    path('products/', ProductListView.as_view(), name="product-list"),
    path('product-features/', FeaturedProductList.as_view(), name="product-features"),
    path('product-detail/<str:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('add-to-cart/', AddToCart.as_view(), name="add-to-cart"),
    path('order-summary/', OrderSummaryPage.as_view(), name="order-summary"),
    path('add-quantity/', AddSingleQuantityToProduct.as_view(), name="add-quantity"),
    path('remove-quantity/', RemoveSingleQuantityFromProduct.as_view(), name="remove-quantity"),
    path('address/', Address.as_view(), name="address"),



]
