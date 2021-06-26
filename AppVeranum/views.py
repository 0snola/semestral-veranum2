from django.shortcuts import redirect, render
from AppVeranum.models import *
from AppVeranum.forms import HabitacionForm, SalonForm

# Create your views here.
def home (request):
    return render(request,'principal.html')

def reservaHabitacion(request):
    if request.method == "POST":
        form = HabitacionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/formulario')
            except:
                pass
    else:
        form = HabitacionForm()
        reservaHabitacion = ReservaHabitacion.objects.all()
        return render(request,'mantenedorReservas.html',{'form': form, 'reservaHabitacion': reservaHabitacion})

def reservaSalon(request):
    if request.method == "POST":
        form = SalonForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/formulario')
            except:
                pass
    else:
        form = SalonForm()
        reservaSalon = ReservaSalon.objects.all()
        return render(request,'mantenedorSalones.html',{'form': form, 'reservaSalon': reservaSalon})


def principal(request):
    return render(request, 'principal.html')

def hotelVina(request):
    return render(request, 'hotelVina.html')          


def hotelSantiago(request):
    return render(request, 'hotelSantiago.html')


def login(request):
    return render(request, 'login.html')    