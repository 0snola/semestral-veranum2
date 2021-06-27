from django.shortcuts import redirect, render
from AppVeranum.models import *
from AppVeranum.forms import HabitacionForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
        return render(request,'formularioHabitacion.html',{'form': form, 'reservaHabitacion': reservaHabitacion})


def principal(request):
    return render(request, 'principal.html')

def hotelVina(request):
    return render(request, 'hotelVina.html')          


def hotelSantiago(request):
    return render(request, 'hotelSantiago.html')



#metodo para el inicio de sesión
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/mantenedor')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('/mantenedor')
            else:
                messages.info(request,'Usuario o password incorrectos')
        return render(request,'login.html',{})

def logoutUser(request):
    logout(request)
    return redirect('login')



#@login_required(login_url='login')
def mantenedor(request):
    if request.method == "POST":
        form = HabitacionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/mantenedor')
            except:
                pass
    else:
        form = HabitacionForm()
        reservaHabitacion = ReservaHabitacion.objects.all()
        return render(request,'mantenedor.html',{'form': form, 'reservaHabitacion': reservaHabitacion})




@login_required(login_url='login')
def editar(request,id_reserva):
    reserva = ReservaHabitacion.objects.get(id=id_reserva)
    form = HabitacionForm(instance=reserva)
    return render(request,'mantenedor_edit.html',{'form': form,'id_reserva':id_reserva})

@login_required(login_url='login')
def update(request,id_reserva):
    reservaHabitacion = ReservaHabitacion.objects.get(id=id_reserva)
    if request.method == "POST":
        form = HabitacionForm(request.POST, instance=reservaHabitacion)
        if form.is_valid():
            form.save()
            return redirect('/mantenedor')

@login_required(login_url='login')
def delete(request,id_reserva):
    reservaHabitacion = ReservaHabitacion.objects.get(id=id_reserva)
    reservaHabitacion.delete()
    return redirect('/mantenedor')    

   