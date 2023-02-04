from django.urls import path
from online_shop.views import get_categories, get_category, get_products, get_product, get_category_products, \
    get_product_of_category


urlpatterns = [
    path('categories', get_categories),
    path('categories/<int:pk>', get_category),
    path('products', get_products),
    path('products/<int:pk>', get_product),
    path('categories/<int:pk>/products', get_category_products),
    path('categories/<int:pk>/products/<int:pk2>', get_product_of_category)
]
