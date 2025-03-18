from django.urls import path
from .views import NoteListCreateView, NoteDetailView, api_notes_page

urlpatterns = [
    path('api/notes/', NoteListCreateView.as_view(), name='note-list'),
    path('api/notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path("api/notes-page/", api_notes_page, name="api_notes_page"),
]
