from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages
from django import template

from django.contrib.auth.models import User

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@require_POST
def payment_method(request):
  customer_email = request.POST.get('emailSub', '')
  plan = request.POST.get('priceId', '')
  customer_id = request.POST.get('customerId', '')
  project_id = request.POST.get('projectId', '')
  automatic = 'on'
  payment_method = 'card'
  context = {}

  payment_intent = stripe.PaymentIntent.create(
    amount='100',
    currency='gbp',
    payment_method_types=['card'],
  )

  if payment_method == 'card':
    context['secret_key'] = payment_intent.client_secret
    context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
    context['customer_email'] = customer_email
    context['payment_intent_id'] = payment_intent.id
    context['automatic'] = automatic
    context['stripe_plan_id'] = plan
    context['customer_id'] = customer_id
    context['project_id'] = project_id

    return render(request, 'payments/card.html', context)


@require_POST
def card(request):
  payment_intent_id = request.POST['payment_intent_id']
  payment_method_id = request.POST['payment_method_id']
  stripe_plan_id = request.POST['stripe_plan_id']
  customer_id = request.POST['customer_id']
  project_id = request.POST['project_id']
  automatic = request.POST['automatic']

  print(f'Project ID: {project_id}')

  print(f'Payment Intent:{payment_intent_id}')

  print(f'Customer Id: {customer_id}')

  # Create new Customer ID if none exists
  customer = None
  if customer_id == '':
    customer = stripe.Customer.create(
      email=request.POST.get('customer_email', ''),
      payment_method=payment_method_id,
      invoice_settings={
        'default_payment_method': payment_method_id
      },
      metadata={
        'userId': request.user.id,
      },
    )
  else:
    customer = stripe.Customer.retrieve(
      customer_id
    )

  if automatic == 'on':
    s = stripe.Subscription.create(
      customer=customer.id,
      items=[
        {
          'plan': stripe_plan_id
        },
      ],
      expand=['latest_invoice.payment_intent'],
      metadata={
        'project_id': project_id
      },
    )

    if s.status == 'incomplete':

      pi = s.latest_invoice.payment_intent.id
      
      stripe.PaymentIntent.modify(
        pi,
        payment_method=payment_method_id,
      )

      ret = stripe.PaymentIntent.confirm(
          pi
        )

      if ret.status == 'requires_action':
        payment_intent = stripe.PaymentIntent.retrieve(
          pi
        )
        context = {}

        context['payment_intent_secret'] = payment_intent.client_secret
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY

        return render(request, 'payments/3dsec.html', context)

  else:
    stripe.PaymentIntent.modify(
      payment_intent_id,
      payment_method=payment_method_id
    )

  return render(request, 'payments/thank_you.html')

