from django import forms
from django.db import models
from django.forms import fields
from AppVeranum.models import Hotel, ReservaHabitacion

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = ReservaHabitacion
        fields = "__all__"