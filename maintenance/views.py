from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import MaintenanceScheduleForm
from .models import MaintenanceSchedule

def  create_or_update_schedule(request, schedule_id=None):
    if schedule_id:
        schedule = get_object_or_404(MaintenanceSchedule, id=schedule_id)
    else:
        schedule = None

    if request.method == 'POST':
        form = MaintenanceScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('list_maintenance_schedule')
    else:
        form = MaintenanceScheduleForm(instance=schedule)

    return render(request, 'maintenance_schedule_form.html', {'form': form})


def list_maintenance_schedule(request):
    status_filter = request.GET.get('status')
    vehicle_id = request.GET.get('vehicle_id')

    schedules = MaintenanceSchedule.objects.all()

    if vehicle_id:
        schedules = schedules.filter(vehicle__id=vehicle_id)

    if status_filter == 'completed':
        schedules = schedules.filter(completed=True)
    elif status_filter == 'not_completed':
        schedules = schedules.filter(completed=False)

    schedules = schedules.order_by('due_date')

    return render(request, 'maintenance_schedule_list.html', {'schedules': schedules})


def delete_maintenance_schedule(request, schedule_id):
    if request.method == "POST":
        schedule = get_object_or_404(MaintenanceSchedule, id=schedule_id)
        schedule.delete()
        return JsonResponse({"message": "Schedule deleted successfully."}, status=200)
    return JsonResponse({"error": "Invalid request method."}, status=400)
