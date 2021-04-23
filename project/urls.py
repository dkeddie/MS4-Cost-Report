from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_project', views.create_project, name='create_project'),
    path('subscribe/<project_id>', views.subscribe, name='subscribe'),
    path('<project_id>/admin/', views.project_admin, name='project_admin'),
    path('add_user/<project_id>/', views.add_user, name='add_user'),
    path('delete_user/<project_id>/<project_user_id>/',
         views.delete_user, name='delete_user'),
]
