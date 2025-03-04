from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_get, name = "login_get"),
    path('logout/', views.logout, name = "logout"),
    path('todos/', views.todos, name = "todos"),
    path('todos/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todos/', views.todo_create, name='todo_create'),
    path('todos/<int:id>/delete/', views.todo_delete, name='todo_delete'),
]
