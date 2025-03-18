from .models import Note
from django import forms

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']