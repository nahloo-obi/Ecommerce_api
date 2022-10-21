
from django.urls import path, include
from .views import ProductListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name="product-list"),
]
