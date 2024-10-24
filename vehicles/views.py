from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import VehicleForm
from .models import Vehicles


# Create your views here.
@login_required(login_url="/auth/login/")
def home(request):
    vehicles = Vehicles.objects.all()
    return render(request, 'vehicles.html', {'vehicles': vehicles})


@login_required(login_url="/auth/login/")
def create_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to home page after creating vehicle
    else:  # Handle GET request to render the form
        form = VehicleForm()

    return render(request, 'vehicle_form.html', {'form': form})

@login_required(login_url="/auth/login/")
def update_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicles, id=vehicle_id)

    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home or the vehicle list after updating
    else:
        form = VehicleForm(instance=vehicle)

    return render(request, 'update_vehicle.html', {'form': form, 'vehicle': vehicle})

@login_required(login_url="/auth/login/")
def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicles, id=vehicle_id)

    if request.method == 'POST':
        vehicle.delete()
        return redirect('home')
