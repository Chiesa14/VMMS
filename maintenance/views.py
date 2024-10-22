from django.shortcuts import render, redirect, get_object_or_404

from .forms import MaintenanceScheduleForm
from .models import MaintenanceSchedule


# Create or Update Maintenance Schedule
def create_or_update_schedule(request, schedule_id=None):
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

    if status_filter == 'completed':
        schedules = MaintenanceSchedule.objects.filter(completed=True).order_by('due_date')
    elif status_filter == 'not_completed':
        schedules = MaintenanceSchedule.objects.filter(completed=False).order_by('due_date')
    else:
        schedules = MaintenanceSchedule.objects.all().order_by('due_date')

    return render(request, 'maintenance_schedule_list.html', {'schedules': schedules})
