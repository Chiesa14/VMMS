from django.contrib.auth.decorators import login_required
from django.db.models import Count
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
        # Get all data for superusers
        vehicles = Vehicles.objects.all()
        users = User.objects.all()
        maintenance_schedule = MaintenanceSchedule.objects.all()
        activities = Activity.objects.all()

        # Chart data for maintenance activities per vehicle
        maintenance_data = (
            maintenance_schedule.values('vehicle__vehicle_name','activities')
            # .annotate(maintenance_count=Count('id'))
        )

        print(maintenance_data)
        data_points = [
            {"label": item["vehicle__vehicle_name"], "y": 2}
            for item in maintenance_data
        ]

        return render(request, 'admin_home.html', {
            'vehicles': vehicles,
            'users': users,
            'maintenance_schedule': maintenance_schedule,
            'activities': activities,
            'vehicles_len': len(vehicles) if vehicles else 0,
            'users_len': len(users) if users else 0,
            'maintenance_schedule_len': len(maintenance_schedule),
            'activities_len': len(activities),
            'current_view': view,
            'data_points': data_points
        })

    elif user.is_staff:
        vehicles = Vehicles.objects.filter(user=user)
        maintenance_data = (
            MaintenanceSchedule.objects.filter(vehicle__user=user)
            .values('vehicle__vehicle_name')
            .annotate(maintenance_count=Count('id'))
        )
        data_points = [
            {"label": item["vehicle__vehicle_name"], "y": item["maintenance_count"]}
            for item in maintenance_data
        ]

        return render(request, 'mechanics_home.html', {
            'vehicles': vehicles,
            'data_points': data_points
        })

    else:
        vehicles = Vehicles.objects.filter(user=user)
        maintenance_data = (
            MaintenanceSchedule.objects.filter(vehicle__user=user)
            .values('vehicle__vehicle_name')
            .annotate(maintenance_count=Count('id'))
        )
        data_points = [
            {"label": item["vehicle__vehicle_name"], "y": item["maintenance_count"]}
            for item in maintenance_data
        ]

        return render(request, 'user_home.html', {
            'vehicles': vehicles,
            'data_points': data_points
        })
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
