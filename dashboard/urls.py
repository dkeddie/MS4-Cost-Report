from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_project', views.create_project, name='create_project'),
    path('project/<project_id>/', views.get_dashboard, name='get_dashboard'),
]
