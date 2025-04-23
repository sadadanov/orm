from django.http import Http404
from django.shortcuts import render

from main.models import Car, Sale


def cars_list_view(request):
    template_name = 'main/list.html'
    cars = Car.objects.all()  # Получаем список всех автомобилей
    context = {'cars': cars}  # Создаем контекст для передачи в шаблон
    return render(request, template_name, context)


def car_details_view(request, car_id):
    template_name = 'main/details.html'
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        raise Http404("Автомобиль с указанным идентификатором не найден.")
    
    context = {'car': car}
    return render(request, template_name, context)


def sales_by_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        sales = Sale.objects.filter(car=car)
        template_name = 'main/sales.html'
        context = {'car': car, 'sales': sales}
        return render(request, template_name, context)
    except Car.DoesNotExist:
        raise Http404('Автомобиль с указанным идентификатором не найден.')
