from django import forms
from django.db import models
from django.db.models.base import Model
from django.forms import fields
from AppVeranum.models import Hotel, ReservaHabitacion, ReservaSalon

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = ReservaHabitacion
        fields = "__all__"

class SalonForm(forms.ModelForm):
    class Meta:
        Model = ReservaSalon
        fields = "__all__"