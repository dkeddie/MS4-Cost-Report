from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth.models import User
from dashboard.models import Project
from .models import ProjectStripeDetails
# from profile.models import UserStripeDetails

import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY
wh_secret = settings.STRIPE_WH_SECRET


@require_POST
@csrf_exempt
def stripe_webhooks(request):
  """
  Stripe webhooks when creating a subscription and initiating payment
  """
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
  # create stripe subscription details
  elif event.type == 'charge.succeeded':
    create_stripe_subscription(request, event.data.object)

  # ... handle other event types
  else:
    print('Unhandled event type {}'.format(event.type))

  return HttpResponse(status=200)


def create_stripe_subscription(request, charge):
  """
  Record to store subscription details
  (Used to retrieve subscription status)
  """
  pi = stripe.PaymentIntent.retrieve(
    charge.payment_intent,
    expand=['invoice']
    )

  sub = stripe.Subscription.retrieve(
    pi.invoice.subscription,
  )

  project = get_object_or_404(Project, id=sub.metadata.project_id)

  obj, created = ProjectStripeDetails.objects.get_or_create(
    project = project,
    customer_id = sub.customer,
    stripe_sub = sub.id,
  )

  # Set project subscription status to True
  # Inital page will load correctly
  project.has_subscription = True
  project.save()

  return HttpResponse(status=200)
