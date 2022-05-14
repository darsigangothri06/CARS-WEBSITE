from django.shortcuts import render, redirect
from .models import Cars
from django.urls import reverse

# Create your views here.


def list_view(request):
    cars = Cars.objects.all()
    return render(request, 'cars/list.html', context={'cars': cars})

def add_view(request):
    if request.POST:
        brand = request.POST['brand']
        year = request.POST['year']
        Cars.objects.create(brand = brand, year = year)
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')

def delete_view(request):
    if request.POST:
        try:
            pk = request.POST['pk']
            Cars.objects.get(pk = pk).delete()
        except:
            pass
        return redirect(reverse('cars:list'))
    return render(request, 'cars/delete.html')