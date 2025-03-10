from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("todos")  # Убедитесь, что такой URL существует
        else:
            return render(request, "login.html", {"error": "Неверные данные"})
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

def todos_view(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos.html', {'todos': todos})

@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'todo_detail.html', {'todo': todo})

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos')
    else:
        form = TodoForm()
    return render(request, 'todo_create.html', {'form': form})

@login_required
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect('todos')

def todo_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todos")  # Редирект обратно к списку
    else:
        form = TodoForm(instance=todo)
    return render(request, "todo_edit.html", {"form": form})