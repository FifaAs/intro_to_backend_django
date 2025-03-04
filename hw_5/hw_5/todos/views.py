from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Todo
from .forms import TodoForm

def login_get(request):
    if request.method == "GET":
        return render(request, "login.html")  # Убедитесь, что есть return
    return render(request, "todo_list.html")  # Или перенаправьте пользователя
    
def login_post(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('')
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('login')

@login_required
def todos(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo_list.html', {'todos':todos})

@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'todo_detail.html', {'todo': todo})

# Создание todo
@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_create.html', {'form': form})

# Удаление todo (только своего)
@login_required
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if todo.user != request.user:
        return HttpResponseForbidden("You can't delete this todo.")
    todo.delete()
    return redirect('todo_list')