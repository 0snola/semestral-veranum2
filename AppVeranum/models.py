from django.forms import ModelForm, TextInput, Textarea
from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel = models.CharField(max_length=100)
    class Meta:
        db_table: "hotel"
    def __str__(self):
        return u'{0}'.format(self.hotel)

class ReservaHabitacion(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    rut = models.IntegerField()
    fecha = models.DateField()
    estadia = models.IntegerField()
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    class Meta:
        db_table: "reservaHabitacion"

class ReservaSalon(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    rut = models.IntegerField()
    fecha = models.DateField()
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    class Meta:
        db_table: "reservaSalon"
    def __str__(self):
        return u'{0}'.format(self.reservaSalon)