from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoListForm, TodoForm
from .models import TodoList, Todo

# Create your views here.
def todo_lists(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')
    else:
        form = TodoListForm()
    
    todos_list = TodoList.objects.all()
    return render(request, 'header.html', {'todos_list': todos_list, 'form': form})

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = Todo.objects.filter(todo_list=todo_list)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  
            post.todo_list = todo_list  
            post.save()  
            return redirect('todo_list_detail', id=todo_list.id)

    else:
        form = TodoForm()

    return render(request, 'base.html', {'todo_list': todo_list, 'todos': todos, 'form': form})

def todo_list_delete(request,id):
    thread = get_object_or_404(TodoList,id=id)
    thread.delete()
    return redirect('todo_lists')

def todo_delete(request,id):
    post = get_object_or_404(Todo, id=id)
    thread_id = post.thread.id 
    post.delete()
    return redirect('todo_list_detail', id=thread_id)


def todo_list_edit(request, id):
    thread = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('todo_lists') 
    else:
        form = TodoListForm(instance=thread)
    
    return render(request, 'header_edit.html', {'form': form, 'thread': thread})




def todo_edit(request, id):
    post = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=post. todo_list.id)  
    else:
        form = TodoForm(instance=post)

    return render(request, 'base_edit.html', {'form': form, 'post': post})
