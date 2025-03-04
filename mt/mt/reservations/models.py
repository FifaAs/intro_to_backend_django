from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField("Имя",max_length=20)
    phone = models.CharField("Телефон",max_length=20)
    
    def __str__(self):
        return self.name

class Table(models.Model):
    number = models.IntegerField("Номер", unique=True)
    seats = models.IntegerField("Число севших")
    is_available = models.BooleanField("Свободно ли",default=True)
    
    def __str__(self):
         return f"Столик №{self.number} ({self.seats} мест)"

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("canceled", "Canceled")], max_length=50)

    def __str__(self):
        return f"Бронь на {self.date} (Клиент: {self.customer.name})"
