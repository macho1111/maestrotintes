from django.urls import path
from .views import apparel_list, apparel_detail, create_product, product_list, product_detail, consent_view
urlpatterns = [
    path('list/', apparel_list, name='apparel_list'),
    path('apparel/<int:apparel_id>/', apparel_detail, name='apparel_detail'),
    path('create_product/', create_product, name='create_product'),
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('', consent_view, name='consent_view'),
]