from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from maintenance.models import MaintenanceSchedule
from .forms import ActivityForm
from .models import Activity


# Create your views here.
def create_activity(request, maintenance_id):
    maintenance = get_object_or_404(MaintenanceSchedule, pk=maintenance_id)  # Retrieve the maintenance record
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.maintenance = maintenance  # Associate the activity with the maintenance
            activity.save()  # Save the activity
            return redirect('list_activities', maintenance.id)
    else:
        form = ActivityForm(maintenance=maintenance)  # Pass the maintenance to the form

    return render(request, 'create_activity.html', {
        'form': form,
        'maintenance': maintenance,  # Pass the maintenance object to the template
    })


def list_activities_by_maintenance(request, maintenance_id):
    maintenance = get_object_or_404(MaintenanceSchedule, pk=maintenance_id)  # Retrieve the maintenance record
    activities = Activity.objects.filter(maintenance=maintenance)  # Fetch activities related to the maintenance

    return render(request, 'list_activities.html', {
        'maintenance': maintenance,
        'activities': activities,
    })


def delete_activity(request, activity_id):
    if request.method == "POST":
        activity = get_object_or_404(Activity, id=activity_id)
        activity.delete()
        return JsonResponse({"message": "Activity deleted successfully."}, status=200)
    return JsonResponse({"error": "Invalid request method."}, status=400)


def mark_as_done(request, activity_id):
    if request.method == 'POST':
        activity = get_object_or_404(Activity, id=activity_id)
        activity.completed = True
        activity.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
