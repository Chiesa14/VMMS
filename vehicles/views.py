from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import VehicleForm
from .models import Vehicles


# Create your views here.
def home(request):
    vehicles = Vehicles.objects.all()
    return render(request, 'vehicles.html', {'vehicles': vehicles})

def create_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to home page after creating vehicle
    else:  # Handle GET request to render the form
        form = VehicleForm()


    return render(request, 'vehicle_form.html', {'form': form})
