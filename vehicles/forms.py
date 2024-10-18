from django import forms

from .models import Vehicles


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = '__all__'
