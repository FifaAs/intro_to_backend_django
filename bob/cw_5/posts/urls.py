from django.urls import path
from .views import category_details, products_details, delete_product, index_category, delete_category, update_category, \
    update_product

urlpatterns = [
    # categories/
    path('', index_category, name='index'),
    path('categories/<int:category_id>/update', update_category, name='update_category'),
    path('categories/<int:category_id>/delete', delete_category, name='delete_category'),
    # products/
    path('categories/<int:category_id>', category_details, name='category_details'),
    path('categories/<int:category_id>/products/<int:product_id>', products_details, name='product_details'),
    path('categories/<int:category_id>/products/<int:product_id>/delete', delete_product, name='delete_product'),
    path('categories/<int:category_id>/products/<int:product_id>/update', update_product, name='update_product'),
]