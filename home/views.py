from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from profile.models import UserProfile, UserStripeDetails
from dashboard.forms import ProjectForm, UserSubDetailsForm
from dashboard.models import Project
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
    subForm = UserSubDetailsForm()
    projects = Project.objects.filter(project_owner_id=user.id)
    stripeProjects = ProjectStripeDetails.objects.filter(project__in=projects)

    try:
      stripeUser = UserStripeDetails.objects.get(user=user)
    except UserStripeDetails.DoesNotExist:
      stripeUser = ""

    for project in projects:
      print(f'Loop: {project.id}')
      
      try:
        project_sub = ProjectStripeDetails.objects.get(project=project.id)
      except ObjectDoesNotExist:
        project_sub = None

      print(project_sub)

      if project_sub is not None:
        print(project)
        subActive = ProjectStripeDetails.sub_status(str(project_sub))
        if subActive == 'active':
          print(f'Project:{project}')
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
      'stripeUser': stripeUser,
      'stripeProjects': stripeProjects,
    }
    return render(request, template, context)

  return redirect('/accounts/login/')
