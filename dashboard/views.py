from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
from django.db.models import Sum
from django import template
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import User
from .models import Change, ChangeAttachments
from project.models import Project
# from profile.models import UserSubscriptionDetails

from .forms import ChangeForm, ChangeAttachmentsForm
from project.forms import ProjectForm

import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY


register = template.Library()




def create_project(request):
  
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




def get_dashboard(request, project_id):
  project = get_object_or_404(Project, id=project_id)
  form = ChangeForm()
  editForm = ChangeForm()
  attachmentsForm = ChangeAttachmentsForm()
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
      'attachmentsForm': attachmentsForm,
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
    attachmentForm = ChangeAttachmentsForm(request.POST, request.FILES)
    files = request.FILES.getlist('attachment')
    project = get_object_or_404(Project, pk=project_id)
    print(attachmentForm.errors)
    if form.is_valid() and attachmentForm.is_valid():
      change = form.save(commit=False)
      change.project_id = project
      change.project_user = request.user
      change.save()
      for f in files:
        file_instance = ChangeAttachments(attachment=f)
        file_instance.save()
        change.attachment.add(file_instance)
      messages.success(request, f'{change.change_name} added to {change.project_id}')

    else:
      if form.is_valid():
        print("form is valid")
      elif attachmentForm.is_valid():
        print("attachmentForm is valid")
      else:
        print("neither forms are valid")

    return redirect(reverse('get_dashboard', args=[project.id]))
    


def edit_change(request, change_id):
  change = get_object_or_404(Change, pk=change_id)

  if request.method == 'POST':
    form = ChangeForm(request.POST)
    attachmentForm = ChangeAttachmentsForm(request.POST, request.FILES)
    files = request.FILES.getlist('attachment')
    project_id_id = change.project_id_id
    if form.is_valid() and attachmentForm.is_valid():
      change = form.save(commit=False)
      change.id = change_id
      change.project_user_id = request.user.id
      change.project_id_id = project_id_id
      change.save()
      for f in files:
        file_instance = ChangeAttachments(attachment=f)
        file_instance.save()
        change.attachment.add(file_instance)
      messages.success(request, f'{change.change_name} has been updated')


    return redirect(reverse('get_dashboard', args=[change.project_id_id]))

  else:
    changeForm = ChangeForm(instance=change)
    attachmentsForm = ChangeAttachmentsForm(instance=change)
    attachments = change.attachment.all()
    template = 'dashboard/edit_change.html'

    context = {
      'changeForm': changeForm,
      'attachmentsForm': attachmentsForm,
      'change': change,
      'attachments': attachments,
    }

    return render(request, template, context)


def delete_file(request, change_id, file_id):
  # Delete an attachment a Change whilst in the Edit Change mode

  attachment = get_object_or_404(ChangeAttachments, pk=file_id)
  attachment.delete()

  return redirect(reverse('edit_change', args=[change_id]))


def delete_change(request, change_id):
  # Delete a Change

  change = get_object_or_404(Change, pk=change_id)

  # Step to delete all attachments and files stored
  attachments = change.attachment.all()
  for a in attachments:
    a.delete()

  change.delete()

  return redirect(reverse('get_dashboard', args=[change.project_id_id]))
