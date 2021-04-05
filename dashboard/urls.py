from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_project', views.create_project, name='create_project'),
    path('project/<project_id>/', views.get_dashboard, name='get_dashboard'),
    # path('subscribe/<project_id>/', views.createSubscription, name='createSubscription'),
    path('payment-method/', views.payment_method, name='payment_method'),
    path('thank_you/', views.card, name='card'),
    path('stripe-webhooks/', views.stripe_webhooks, name='stripe_webhooks'),
    # path('subscription/', views.createSubscription, name='createSubscription'),
    path('add_change/<project_id>/', views.add_change, name='add_change'),
    path('edit_change/<change_id>/', views.edit_change, name='edit_change'),
    path('delete_file/<change_id>/<file_id>/', views.delete_file, name='delete_file'),
    path('delete_change/<change_id>/', views.delete_change, name='delete_change'),
]
