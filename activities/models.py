from django.db import models

from maintenance.models import MaintenanceSchedule


# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    maintenance = models.ForeignKey(MaintenanceSchedule, on_delete=models.CASCADE, related_name='activities')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.maintenance}'

    class Meta:
        db_table = 'activities'