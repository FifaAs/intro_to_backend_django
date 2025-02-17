from django.urls import path
from . import views

urlpatterns = [
    path('',views.todo_lists,name='todo_lists'),#b
    path('<int:id>/',views.todo_list_detail,name='todo_list_detail'),#c
    path('<int:id>/delete/',views.todo_list_delete,name='todo_list_delete'),#d
    path('<int:id>/edit/', views.todo_list_edit, name='todo_list_edit'),#e
    path('todos/<int:id>/delete/', views.todo_delete, name='todo_delete'),#f
    path('todos/<int:id>/edit/', views.todo_edit, name='todo_edit'),#g
]