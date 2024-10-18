from django.contrib import admin
from .models import Vehicles

# Register your models here.

@admin.register(Vehicles)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make','vehicle_name','model','year','vin')
    search_fields = ('make','model','vin')