from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.

def todo_list(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    
    todos = Todo.objects.all()
    return render(request, 'todos.html', {'todos': todos, 'form': form})

def todo_delete(request,id):
    todo = get_object_or_404(Todo,id=id)
    todo.delete()
    return redirect('todo_list')

def todo_detail(request,id):
    todo = get_object_or_404(Todo,id=id)
    return render(request,'todo.html',{'todo':todo})
