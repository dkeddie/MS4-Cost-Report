from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
from django.db.models import Sum
from django import template
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

from django.contrib.auth.models import User
from .models import Project, Change, Project_StripeDetails
from profile.models import UserSubDetails
from profile.models import UserStripeDetails

from .forms import ProjectForm, ChangeForm, UserSubDetailsForm

import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY


register = template.Library()


@require_POST
@csrf_exempt
def stripe_webhooks(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, settings.STRIPE_WH_SECRET
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
  # print(f"set paid until {charge}")
  pi = stripe.PaymentIntent.retrieve(
    charge.payment_intent,
    expand=['invoice']
    )

  # print(f'Set paid unitl PI: {pi}')

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

  obj2, created2 = Project_StripeDetails.objects.get_or_create(
    project = get_object_or_404(Project, id=sub.metadata.project_id),
    stripe_sub = sub.id,
  )

  return HttpResponse(status=200)


def create_project(request):
  project = get_object_or_404(Project, pk=1)
  if request.method == 'POST':
    form = ProjectForm(request.POST)
    if form.is_valid():
      project = form.save(commit=False)
      project.project_owner = request.user
      project.save()
      messages.success(request, f'{project.project_name} created')

    context = {
      'project': project,
    }

    return redirect(reverse('home'))


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
    return render(request, 'home/card.html', context)


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

        return render(request, 'home/3dsec.html', context)

  else:
    stripe.PaymentIntent.modify(
      payment_intent_id,
      payment_method=payment_method_id
    )

  return render(request, 'home/thank_you.html')


def get_dashboard(request, project_id):
  project = get_object_or_404(Project, id=project_id)
  form = ChangeForm()
  editForm = ChangeForm()
  changes = Change.objects.filter(project_id=project_id)

  original_estimate = project.original_estimate
  
  accepted_changes = Change.objects.filter(project_id=project_id, change_status="A").aggregate(Sum('change_cost'))['change_cost__sum']
  if accepted_changes is None:
    accepted_changes = 0

  pending_changes = Change.objects.filter(project_id=project_id, change_status="P").aggregate(Sum('change_cost'))['change_cost__sum']
  if pending_changes is None:
    pending_changes = 0

  wip_changes = Change.objects.filter(project_id=project_id, change_status="WiP").aggregate(Sum('change_cost'))['change_cost__sum']
  if wip_changes is None:
    wip_changes = 0

  rejected_changes = Change.objects.filter(project_id=project_id, change_status="R").aggregate(Sum('change_cost'))['change_cost__sum']
  if rejected_changes is None:
    rejected_changes = 0

  subtotal = original_estimate + accepted_changes
  total = subtotal + pending_changes + wip_changes

  if request.user.id is project.project_owner_id:
    context = {
      'project': project,
      'form': form,
      'editForm': editForm,
      'changes': changes,
      'original_estimate': original_estimate,
      'accepted_changes': accepted_changes,
      'pending_changes': pending_changes,
      'wip_changes': wip_changes,
      'rejected_changes': rejected_changes,
      'subtotal': subtotal,
      'total': total,
    }

    return render(request, 'dashboard/project.html', context)


def add_change(request, project_id):

  if request.method == 'POST':
    form = ChangeForm(request.POST)
    project = get_object_or_404(Project, pk=project_id)
    if form.is_valid():
      change = form.save(commit=False)
      change.project_id = project
      change.project_user = request.user
      change.save()
      messages.success(request, f'{change.change_name} added to {change.project_id}')

    return redirect(reverse('get_dashboard', args=[project.id]))


def edit_change(request, change_id):
  change = get_object_or_404(Change, pk=change_id)

  if request.method == 'POST':
    editForm = ChangeForm(request.POST)
    project_user_id = change.project_user_id
    project_id_id = change.project_id_id
    if editForm.is_valid():
      print(change)
      change = editForm.save(commit=False)
      change.id = change_id
      change.project_user_id = project_user_id
      change.project_id_id = project_id_id
      change.save()
      messages.success(request, f'{change.change_name} has been updated')


    return redirect(reverse('get_dashboard', args=[change.project_id_id]))

  else:
    change_dict = model_to_dict(change)
    print(change_dict)
    return JsonResponse(change_dict, safe=False)

