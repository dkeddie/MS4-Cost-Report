from django.shortcuts import render, get_object_or_404, redirect, reverse
from django import template

from .models import Project, Change
from .forms import ProjectForm, ChangeForm

register = template.Library()

def create_project(request):
  project = get_object_or_404(Project, pk=1)
  if request.method == 'POST':
    form = ProjectForm(request.POST)
    if form.is_valid():
      project = form.save(commit=False)
      project.project_owner = request.user
      project.save()
      print("Project saved")

    context = {
      'project': project,
    }

    return render(request, 'dashboard/dashboard.html', context)


def get_dashboard(request, project_id):
  project = get_object_or_404(Project, id=project_id)
  form = ChangeForm()
  changes = Change.objects.filter(project_id=project_id)

  if request.user.id is project.project_owner_id:
    context = {
      'project': project,
      'form': form,
      'changes': changes,
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
      print("Change saved")

    return redirect(reverse('get_dashboard', args=[project.id]))

