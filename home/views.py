from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from profile.models import UserProfile, UserStripeDetails
from dashboard.forms import ProjectForm, UserSubDetailsForm
from dashboard.models import Project


def index(request):
  """ A view to return the index page """
  user = request.user

  if request.user.is_authenticated:
    registration = user
    profile = get_object_or_404(UserProfile, user=user)
    form = ProjectForm()
    subForm = UserSubDetailsForm()
    projects = Project.objects.filter(project_owner_id=user.id)
    stripeUser = get_object_or_404(UserStripeDetails, user=user) or ""

    template = 'home/index.html'
    context = {
      'registration': registration,
      'profile': profile,
      'form': form,
      'subForm': subForm,
      'projects': projects,
      'stripeUser': stripeUser,
    }
    return render(request, template, context)

  return redirect('/accounts/login/')