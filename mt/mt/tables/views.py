from django.shortcuts import render, get_object_or_404, redirect
from .models import Table, Reservation

from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import Table

def tables(request):
    if request.method == "POST":
        number = request.POST.get("number")
        seats = request.POST.get("seats")
        
        # Проверка: существует ли столик с таким номером
        if Table.objects.filter(number=number).exists():
            return render(request, "tables/tables.html", {
                "error": f"Столик #{number} уже существует!",
                "tables": Table.objects.all(),
            })

        try:
            Table.objects.create(number=number, seats=seats)
        except IntegrityError:
            return render(request, "tables/tables.html", {
                "error": "Ошибка базы данных. Попробуйте снова.",
                "tables": Table.objects.all(),
            })

        return redirect("table-list-create")  # Перенаправляем после успешного создания

    tables = Table.objects.all()
    return render(request, "tables/tables.html", {"tables": tables})



def tables_available(request):
    # Столики, у которых нет подтвержденных броней
    reserved_tables = Reservation.objects.filter(status="confirmed").values_list("table_id", flat=True)
    tables = Table.objects.exclude(id__in=reserved_tables)  # Только свободные столики

    return render(request, "tables/tables_available.html", {"tables": tables})
