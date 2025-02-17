from django import forms
from .models import Todo, TodoList

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'description']
        widgets = {
            "title": forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Название"
            }),
            "description": forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': "Описание",
                'rows': 3
            })
        }

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status']
    
        widgets={ 
              "title": forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Название"
              }),
              "description": forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Описание",
                'rows': 3
              }),
              "due_date": forms.DateInput(attrs={
                'class':"form-control",
                'placeholder':"Дата",
                'rows': 6
              }),
              "status": forms.CheckboxInput(attrs={
                'class': "form-check-input"
              })
              
         }

