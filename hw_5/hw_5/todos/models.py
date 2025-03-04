from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField("Название",max_length=20)
    description = models.TextField("Описание")
    due_date = models.DateField("Дата")
    status = models.BooleanField("Статус", default=False)
    todo_list = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

