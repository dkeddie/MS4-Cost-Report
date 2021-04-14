from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from profile.models import UserProfile
from profile.forms import UserSubscriptionDetailsForm

from project.models import Project
from project.forms import ProjectForm

from payments.models import ProjectStripeDetails

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
  """ A view to return the index page """
  user = request.user

  if request.user.is_authenticated:
    registration = user
    profile = get_object_or_404(UserProfile, user=user)
    form = ProjectForm()
    subForm = UserSubscriptionDetailsForm()
    projects = Project.objects.filter(project_owner_id=user.id)
    stripeProjects = ProjectStripeDetails.objects.filter(project__in=projects)

    print(projects)

    for project in projects:
    
      try:
        project_sub = ProjectStripeDetails.objects.get(project=project.id)
      except ObjectDoesNotExist:
        project_sub = None

      if project_sub is not None:
        subActive = ProjectStripeDetails.sub_status(project_sub)
        if subActive == 'active':
          project.has_subscription=True
          project.save()
        else:
          project.has_subscription=False
          project.save

      else:
        project.has_subscription=False
        project.save()


    template = 'home/index.html'
    context = {
      'registration': registration,
      'profile': profile,
      'form': form,
      'subForm': subForm,
      'projects': projects,
      'stripeProjects': stripeProjects,
    }
    return render(request, template, context)

  return redirect('/accounts/login/')
