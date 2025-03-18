from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer

# Список заметок и создание новых (GET, POST)
class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Получение, обновление и удаление заметки (GET, PUT, DELETE)
class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

def api_notes_page(request):
    return render(request, "main.html")