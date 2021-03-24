from django.shortcuts import render, get_object_or_404

from .models import Project
from .forms import ProjectForm

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

  if request.user.id is project.project_owner_id:
    context = {
      'project': project
    }

    return render(request, 'dashboard/project.html', context)
