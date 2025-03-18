from django.shortcuts import render
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
from django.http import HttpRequest

def note_list(request: HttpRequest):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes})

def note_create(request: HttpRequest):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form})

def note_edit(request: HttpRequest, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_form.html', {'form': form})

def note_delete(request: HttpRequest, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'note_confirm_delete.html', {'note': note})
