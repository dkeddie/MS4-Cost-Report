from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import template

from django.contrib.auth.models import User

from profile.models import UserSubscriptionDetails
from profile.forms import UserSubscriptionDetailsForm

from project.models import Project

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
@require_POST
def payment_method(request):
    """
    Payment Page - retrieves subscription method and loads card payment page
    """
    customer_email = request.POST.get('emailSub', '')
    customer_name = request.POST.get('nameSub', '')
    plan = request.POST.get('priceId', '')
    customer_id = request.POST.get('customerId', '')
    project_id = request.POST.get('projectId', '')
    automatic = 'on'
    payment_method = 'card'

    try:
        user = UserSubscriptionDetails.objects.get(user=request.user) or None
        form = UserSubscriptionDetailsForm(instance=user)
    except UserSubscriptionDetails.DoesNotExist:
        form = UserSubscriptionDetailsForm()

    # RETRIEVE THE PRICE OF THE SUBSCRIPTION SELECTED
    price = stripe.Price.retrieve(plan).unit_amount

    context = {}

    # CREATE PAYMENT INTENT FOR STRIPE
    payment_intent = stripe.PaymentIntent.create(
        amount=price,
        currency='gbp',
        payment_method_types=['card'],
    )

    # INFORMATION REQUIRED FOR PAYMENT PAGE
    if payment_method == 'card':
        context['secret_key'] = payment_intent.client_secret
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        context['customer_email'] = customer_email
        context['payment_intent_id'] = payment_intent.id
        context['automatic'] = automatic
        context['stripe_plan_id'] = plan
        context['customer_id'] = customer_id
        context['customer_name'] = customer_name
        context['project_id'] = project_id
        context['form'] = form

        return render(request, 'payments/card.html', context)


@login_required
@require_POST
def card(request):
    """
    Process card payment details through stripe
    """
    payment_intent_id = request.POST['payment_intent_id']
    payment_method_id = request.POST['payment_method_id']
    stripe_plan_id = request.POST['stripe_plan_id']
    customer_id = request.POST['customer_id']
    project_id = request.POST['project_id']
    automatic = request.POST['automatic']

    # SAVE / UPDATE USER PAYMENT DETAILS
    try:
        userSub = UserSubscriptionDetails.objects.get(user=request.user)
        form = UserSubscriptionDetailsForm(request.POST, instance=userSub)
    except UserSubscriptionDetails.DoesNotExist:
        userSub = None
        form = UserSubscriptionDetailsForm(request.POST)

    # User details are saved as it is a subscription
    if form.is_valid():
        if userSub is None:
            sub = form.save(commit=False)
            sub.user = request.user
            sub.save()
        else:
            sub = form.save()

    det = get_object_or_404(UserSubscriptionDetails, user=sub.user)

    # Create new Customer ID if none exists
    customer = None
    customer = stripe.Customer.create(
        email=request.POST.get('customer_email', ''),
        name=request.POST.get('customer_name', ''),
        phone=det.default_phone_number,
        payment_method=payment_method_id,
        invoice_settings={
            'default_payment_method': payment_method_id
        },
        metadata={
            'userId': request.user.id,
        },
        address={
            'line1': det.default_street_address1,
            'line2': det.default_street_address2,
            'city': det.default_town_or_city,
            'country': det.default_country,
            'state': det.default_county,
            'postal_code': det.default_postcode,
        },
    )

    # Creates Subscription on stripe
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

        # Once subscription created, Payment Intent needs completing
        if s.status == 'incomplete':
            pi = s.latest_invoice.payment_intent.id
            stripe.PaymentIntent.modify(
                pi,
                payment_method=payment_method_id,
            )
            ret = stripe.PaymentIntent.confirm(
                pi
            )

            # Payments which require 3D authentication
            if ret.status == 'requires_action':
                payment_intent = stripe.PaymentIntent.retrieve(
                    pi
                )
                context = {}

                context['payment_intent_secret'] = payment_intent.client_secret
                context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
                context['project_id'] = project_id
                context['customer_email'] = request.POST.get('customer_email', '')
                context['project'] = get_object_or_404(Project, pk=project_id)

                return render(request, 'payments/3dsec.html', context)

    else:
        stripe.PaymentIntent.modify(
            payment_intent_id,
            payment_method=payment_method_id
        )

    project = get_object_or_404(Project, pk=project_id)

    context = {
        'project': project,
        'project_id': project_id,
        'customer_email': request.POST.get('customer_email', ''),
    }

    return render(request, 'payments/thank_you.html', context)


@login_required
@require_POST
def customer_portal(request, stripe_user, project_id):
    """
    Link to stripe subscription portal
    """
    # static url of page
    return_url = request.build_absolute_uri('/project/')

    # returns session specific url to access stripe portal
    session = stripe.billing_portal.Session.create(
        customer=stripe_user,
        return_url=f'{return_url}{project_id}/admin',
    )
    return redirect(session.url)


def customer_portal_email(request, stripe_user):
    """
    Link to stripe subscription portal from email
    Used when Project deleted and no Customer Portal not accessible
    through webpage
    """
    return_url = request.build_absolute_uri(reverse('home'))
    session = stripe.billing_portal.Session.create(
        customer=stripe_user,
        return_url=f'{return_url}'
    )
    return redirect(session.url)
