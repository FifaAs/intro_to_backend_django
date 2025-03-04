from django.urls import path
from .views import tables, tables_available

urlpatterns = [
    path('', tables, name='table-list-create'),
    path('available/', tables_available, name='available-tables'),
]
