from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from activities.models import Activity
from maintenance.models import MaintenanceSchedule
from users.models import User
from .forms import VehicleForm
from .models import Vehicles


# Create your views here.
@login_required(login_url="/auth/login/")
@login_required(login_url="/auth/login/")
def home(request):
    view = request.GET.get("view", "vehicles")
    user = request.user

    if user.is_superuser:
        vehicles = Vehicles.objects.all()
        users = User.objects.all()
        maintenance_schedule = MaintenanceSchedule.objects.all()
        activities = Activity.objects.all()

        return render(request, 'admin_home.html', {
            'vehicles': vehicles,
            'users': users,
            'maintenance_schedule': maintenance_schedule,
            'activities': activities,
            'vehicles_len': len(vehicles) if vehicles else 0,
            'users_len': len(users) if users else 0,
            'maintenance_schedule_len': len(maintenance_schedule),
            'activities_len': len(activities),
            'current_view': view
        })

    elif user.is_staff:
        vehicles = Vehicles.objects.filter(user=user)
        return render(request, 'mechanics_home.html', {'vehicles': vehicles})

    else:
        vehicles = Vehicles.objects.filter(user=user)
        return render(request, 'user_home.html', {'vehicles': vehicles})

@login_required(login_url="/auth/login/")
def create_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
            return redirect('home')
    else:
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
