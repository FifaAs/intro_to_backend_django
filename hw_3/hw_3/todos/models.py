from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField("Название",max_length=20)
    description = models.TextField("Описание")
    due_date = models.DateField("Дата")
    status = models.BooleanField("Статус")

    def __str__(self):
        return self.title

