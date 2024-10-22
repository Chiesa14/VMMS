from django import forms

from .models import MaintenanceSchedule


class MaintenanceScheduleForm(forms.ModelForm):
    class Meta:
        model = MaintenanceSchedule
        fields = '__all__'
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }