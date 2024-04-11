from django.urls import path
from .views import apparel_list, apparel_detail, create_product, ProductListView, ProductDetailView, ConsentView
urlpatterns = [
    path('list/', apparel_list, name='apparel_list'),
    path('apparel/<int:apparel_id>/', apparel_detail, name='apparel_detail'),
    path('create_product/', create_product, name='create_product'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('', ConsentView.as_view(), name='consent_view'),
]