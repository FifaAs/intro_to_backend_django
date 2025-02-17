from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField("Название",max_length=20)
    link = models.URLField("ссылка")
    

    def __str__(self):
        return self.title

