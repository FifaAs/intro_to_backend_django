from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Reservation

def customers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        if name and phone:
            Customer.objects.create(name=name, phone=phone)
        return redirect('customer-list-create')

    customers = Customer.objects.all()
    return render(request, 'customers/customers.html', {'customers': customers})



def customers_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    reservations = Reservation.objects.filter(customer=customer).select_related('table')
    
    return render(request, 'customers/customer_detail.html', {
        'customer': customer,
        'reservations': reservations
    })
