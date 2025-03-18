from django.db import models
from django.utils.timezone import now

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateField(default=now)