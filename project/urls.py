from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<project_id>/admin/', views.project_admin, name='project_admin'),
    path('add_user/<project_id>/', views.add_user, name='add_user'),
    path('delete_user/<project_user_id>/', views.delete_user, name='delete_user'),
]
