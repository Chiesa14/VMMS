from django import forms
from .models import Vehicles

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['vin'].disabled = True
            self.fields['type'].disabled = True
