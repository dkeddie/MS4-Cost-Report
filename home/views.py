from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from profile.models import UserProfile
from dashboard.forms import ProjectForm


def index(request):
  """ A view to return the index page """
  user = request.user

  if request.user.is_authenticated:
    registration = user
    profile = get_object_or_404(UserProfile, user=user)
    form = ProjectForm()

    template = 'home/index.html'
    context = {
      'registration': registration,
      'profile': profile,
      'form': form,
    }
    return render(request, template, context)

  return redirect('/accounts/login/')