from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Sum
from django import template
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

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
      print("Change saved")

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

    return redirect(reverse('get_dashboard', args=[change.project_id_id]))

  else:
    change_dict = model_to_dict(change)
    print(change_dict)
    return JsonResponse(change_dict, safe=False)

