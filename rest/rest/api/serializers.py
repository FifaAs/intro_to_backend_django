from rest_framework import serializers

from rest_framework import serializers
from .models import Note  # Импортируем модель Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'  # Выведем все поля