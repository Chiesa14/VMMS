from django.urls import path

from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('create/', views.create_vehicle, name='create_vehicle'),
    path('update/<int:vehicle_id>/', views.update_vehicle, name='update_vehicle'),
]