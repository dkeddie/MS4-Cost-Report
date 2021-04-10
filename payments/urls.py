from django.contrib import admin
from django.urls import path
from . import views, webhooks

urlpatterns = [
    path('payment-method/', views.payment_method, name='payment_method'),
    path('thank_you/', views.card, name='card'),
    path('stripe-webhooks/', webhooks.stripe_webhooks, name='stripe_webhooks'),
]
