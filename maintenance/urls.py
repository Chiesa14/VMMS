from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_maintenance_schedule, name='list_maintenance_schedule'),


    path('create/', views.create_or_update_schedule, name='create_maintenance_schedule'),
    path('<int:schedule_id>/update/', views.create_or_update_schedule, name='update_maintenance_schedule'),
]
