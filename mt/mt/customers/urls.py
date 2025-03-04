from django.urls import path
from .views import customers, customers_detail

urlpatterns = [
    path('', customers, name='customer-list-create'),
    path('<int:pk>/', customers_detail, name='customer_detail'),
]
