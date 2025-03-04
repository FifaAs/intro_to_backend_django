from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from tables.models import Table
from customers.models import Customer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def create_reservation(request):
    customers = Customer.objects.all()
    tables = Table.objects.filter(is_available=True)
    reservations = Reservation.objects.all()
    
    if request.method == "POST":
        customer_id = request.POST.get('customer_id')
        table_id = request.POST.get('table_id')
        date = request.POST.get('date')
        
        customer = get_object_or_404(Customer, id=customer_id)
        table = get_object_or_404(Table, id=table_id)
        
        existing_reservation = Reservation.objects.filter(table=table, date=date).exists()
        user_reservation = Reservation.objects.filter(customer=customer, date=date).exists()
        
        if existing_reservation:
            return JsonResponse({'error': 'Table is already reserved for this date'}, status=400)
        if user_reservation:
            return JsonResponse({'error': 'User already has a reservation for this date'}, status=400)
        
        reservation = Reservation.objects.create(
                    customer=customer,
                    table=table,
                    date=date,
                    status='pending'
        )
        table.is_available = False
        table.save()
        return redirect('create_reservation')
    
    return render(request, 'reservations/create.html', {'customers': customers, 'tables': tables, 'reservations': reservations})

def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return render(request, 'reservations/detail.html', {'reservation': reservation})

def user_reservations(request, user_id):
    reservations = Reservation.objects.filter(customer__id=user_id)
    return render(request, 'reservations/user_reservations.html', {'reservations': reservations})

@csrf_exempt
def update_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == "POST":
        data = json.loads(request.body)
        reservation.status = data.get('status', reservation.status)
        reservation.save()
        return JsonResponse({'message': 'Reservation updated'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def delete_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.delete()
    return redirect('create_reservation')