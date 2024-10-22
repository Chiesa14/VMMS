from django.db import models

from vehicles.models import Vehicles


# Create your models here.
class MaintenanceSchedule(models.Model):
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE, related_name='maintenance_schedule')
    task_name = models.CharField(max_length=255)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Scheduled: {self.task_name} for {self.vehicle.vehicle_name}"

    class Meta:
        db_table = 'maintenance_schedule'