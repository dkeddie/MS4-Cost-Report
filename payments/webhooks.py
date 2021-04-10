from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth.models import User
from dashboard.models import Project
from .models import ProjectStripeDetails
from profile.models import UserStripeDetails

import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY
wh_secret = settings.STRIPE_WH_SECRET


@require_POST
@csrf_exempt
def stripe_webhooks(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, wh_secret
    )
    print("Event constructed accordingly")
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the event
  if event.type == 'payment_intent.succeeded':
    payment_intent = event.data.object # contains a stripe.PaymentIntent
    print('PaymentIntent was successful!')
  elif event.type == 'payment_method.attached':
    payment_method = event.data.object # contains a stripe.PaymentMethod
    print('PaymentMethod was attached to a Customer!')
  # set paid until
  elif event.type == 'charge.succeeded':
    set_paid_until(request, event.data.object)

  # ... handle other event types
  else:
    print('Unhandled event type {}'.format(event.type))

  return HttpResponse(status=200)


def set_paid_until(request, charge):
  pi = stripe.PaymentIntent.retrieve(
    charge.payment_intent,
    expand=['invoice']
    )

  customer = None

  if pi.customer:
    customer = stripe.Customer.retrieve(
      pi.customer,
      expand=['subscriptions']
      )

  obj, created = UserStripeDetails.objects.get_or_create(
    user = get_object_or_404(User, id=customer.metadata.userId),
    stripe_customer_id = customer.id,
  )

  sub = stripe.Subscription.retrieve(
    pi.invoice.subscription,
  )

  obj2, created2 = ProjectStripeDetails.objects.get_or_create(
    project = get_object_or_404(Project, id=sub.metadata.project_id),
    stripe_sub = sub.id,
  )

  return HttpResponse(status=200)
