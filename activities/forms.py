from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'details', 'completed']  # Exclude maintenance from the visible fields

    def __init__(self, *args, **kwargs):
        maintenance = kwargs.pop('maintenance', None)  # Pop maintenance from kwargs
        super().__init__(*args, **kwargs)

        # Add the maintenance ID as a hidden field if maintenance is provided
        if maintenance:
            self.fields['maintenance'] = forms.CharField(
                widget=forms.HiddenInput(),
                initial=maintenance.id
            )
