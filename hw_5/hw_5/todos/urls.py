from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from todos.views import *

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("todos/", todos_view, name="todos"),
    path('todos/<int:id>/', todo_detail, name='todo_detail'),
    path('todos/create/', todo_create, name='todo_create'),
    path('todos/<int:id>/delete/', todo_delete, name='todo_delete'),
    path("todos/<int:id>/edit/", todo_edit, name="todo_edit"),
]
