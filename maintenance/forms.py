from django import forms

from .models import MaintenanceSchedule


class MaintenanceScheduleForm(forms.ModelForm):
    class Meta:
        model = MaintenanceSchedule
        fields = ('task_name','due_date')
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }