from django.urls import  path
from  . import   views

urlpatterns = [
    path('activity/create/<int:maintenance_id>/', views.create_activity, name='create_activity'),
    path('activity/<int:maintenance_id>/activities/', views.list_activities_by_maintenance, name='list_activities'),
    path('activity/activities/', views.list_activities_as_admin, name='list_activities_as_admin'),
    path('activity/<int:activity_id>/delete', views.delete_activity, name='delete_activity'),
    path('schedule/<int:activity_id>/mark_as_done/', views.mark_as_done, name='mark_as_done'),

]