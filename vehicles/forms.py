from django import forms
from .models import Vehicles

class VehicleForm(forms.ModelForm):
    year = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Issued Date'}))
    vehicle_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Vehicle Name'}))
    color = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Vehicle Color'}))
    vin = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Unique Car Identifier'}))
    make = forms.ChoiceField(choices=[('', 'Select the car maker')] + list(Vehicles.MAKE_CHOICES))
    model = forms.ChoiceField(choices=[('', 'Select the car model')] + list(Vehicles.MODEL_CHOICES))
    type = forms.ChoiceField(choices=[('', 'Select type')] + list(Vehicles.TYPE_CHOICES))

    class Meta:
        model = Vehicles
        fields = ('make','vehicle_name','model','year','vin','color','type')

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['vin'].disabled = True
            self.fields['type'].disabled = True
