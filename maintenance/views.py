from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from vehicles.models import Vehicles
from .forms import MaintenanceScheduleForm
from .models import MaintenanceSchedule


@login_required(login_url="/auth/login/")
def create_or_update_schedule(request, schedule_id=None, ):
    schedule = get_object_or_404(MaintenanceSchedule, id=schedule_id) if schedule_id else None

    vehicle_id = request.GET.get('vehicle_id', None)
    if vehicle_id:
        vehicle = get_object_or_404(Vehicles, id=vehicle_id)
    else:
        return redirect('home')

    if request.method == 'POST':
        form = MaintenanceScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.vehicle = vehicle
            schedule.save()
            return redirect(f"{reverse('list_maintenance_schedule')}?vehicle_id={vehicle_id}")
    else:
        form = MaintenanceScheduleForm(instance=schedule)

    return render(request, 'maintenance_schedule_form.html', {'form': form})


@login_required(login_url="/auth/login/")
def list_maintenance_schedule(request):
    status_filter = request.GET.get('status')
    vehicle_id = request.GET.get('vehicle_id')

    schedules = MaintenanceSchedule.objects.all()

    if vehicle_id:
        schedules = schedules.filter(vehicle__id=vehicle_id)
    if vehicle_id and status_filter == 'completed':
        schedules = schedules.filter(completed=True)
    elif vehicle_id and status_filter == 'not_completed':
        schedules = schedules.filter(completed=False)

    if not vehicle_id and not status_filter == 'completed' or not vehicle_id and not status_filter == 'not_completed':
        return redirect('home')

    schedules = schedules.order_by('due_date')

    return render(request, 'maintenance_schedule_list.html', {'schedules': schedules})


@login_required(login_url="/auth/login/")
def delete_maintenance_schedule(request, schedule_id):
    if request.method == "POST":
        schedule = get_object_or_404(MaintenanceSchedule, id=schedule_id)
        schedule.delete()
        return JsonResponse({"message": "Schedule deleted successfully."}, status=200)
    return JsonResponse({"error": "Invalid request method."}, status=400)
