from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from profile.models import UserProfile
from dashboard.forms import ProjectForm
from dashboard.models import Project


def index(request):
  """ A view to return the index page """
  user = request.user

  if request.user.is_authenticated:
    registration = user
    profile = get_object_or_404(UserProfile, user=user)
    form = ProjectForm()
    projects = Project.objects.filter(project_owner_id=user.id)

    template = 'home/index.html'
    context = {
      'registration': registration,
      'profile': profile,
      'form': form,
      'projects': projects,
    }
    return render(request, template, context)

  return redirect('/accounts/login/')