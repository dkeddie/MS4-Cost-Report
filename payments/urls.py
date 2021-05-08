from django.contrib import admin
from django.urls import path
from . import views, webhooks

urlpatterns = [
    path('payment-method/', views.payment_method, name='payment_method'),
    path('thank_you/', views.card, name='card'),
    path('customer-portal/<stripe_user>/<project_id>', views.customer_portal, name='customer_portal'),
    path('customer-portal-email/<stripe_user>/', views.customer_portal_email, name='customer_portal_email'),
    path('stripe-webhooks/', webhooks.stripe_webhooks, name='stripe_webhooks'),
]
