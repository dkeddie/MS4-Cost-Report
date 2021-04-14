from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('project/<project_id>/', views.get_dashboard, name='get_dashboard'),
    path('add_change/<project_id>/', views.add_change, name='add_change'),
    path('edit_change/<change_id>/', views.edit_change, name='edit_change'),
    path('delete_file/<change_id>/<file_id>/', views.delete_file, name='delete_file'),
    path('delete_change/<change_id>/', views.delete_change, name='delete_change'),
]
