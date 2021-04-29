from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.contrib import messages
from django.utils.safestring import mark_safe

from django.db.models import Sum
from django import template

from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from .models import Change, ChangeAttachments
from .forms import ChangeForm, ChangeAttachmentsForm

from django.contrib.auth.models import User
from project.models import Project, ProjectUser

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


register = template.Library()


@login_required
def get_dashboard(request, project_id):
    """
    Load Project Dashboard to display Latest Cost Estimate and List of Changes
    """
    project = get_object_or_404(Project, id=project_id)

    # required to determine permission of user, if not a project user then project owner
    try:
        project_user = ProjectUser.objects.get(
            project=project, project_user=request.user)
    except ProjectUser.DoesNotExist:
        project_user = None

    form = ChangeForm()
    editForm = ChangeForm()
    attachmentsForm = ChangeAttachmentsForm()
    changes = Change.objects.filter(project_id=project_id)

    # Calculations to display on dashboard
    original_estimate = project.original_estimate

    accepted_changes = Change.objects.filter(
        project_id=project_id, change_status="A").aggregate(Sum('change_cost'))['change_cost__sum']
    if accepted_changes is None:
        accepted_changes = 0

    pending_changes = Change.objects.filter(project_id=project_id, change_status="P").aggregate(
        Sum('change_cost'))['change_cost__sum']
    if pending_changes is None:
        pending_changes = 0

    wip_changes = Change.objects.filter(project_id=project_id, change_status="WiP").aggregate(
        Sum('change_cost'))['change_cost__sum']
    if wip_changes is None:
        wip_changes = 0

    rejected_changes = Change.objects.filter(
        project_id=project_id, change_status="R").aggregate(Sum('change_cost'))['change_cost__sum']
    if rejected_changes is None:
        rejected_changes = 0

    subtotal = original_estimate + accepted_changes
    total = subtotal + pending_changes + wip_changes

    if request.user.id is project.project_owner_id or project.project_users:
        context = {
            'project': project,
            'project_user': project_user,
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


@login_required
def add_change(request, project_id):
    """
    Add a new change to List of Changes
    """

    if request.method == 'POST':
        form = ChangeForm(request.POST)
        attachmentForm = ChangeAttachmentsForm(request.POST, request.FILES)
        files = request.FILES.getlist('attachment')
        project = get_object_or_404(Project, pk=project_id)
        if form.is_valid() and attachmentForm.is_valid():
            change = form.save(commit=False)
            change.project_id = project
            change.project_user = request.user
            change.save()
            for f in files: # possible to upload multiple files
                file_instance = ChangeAttachments(attachment=f)
                file_instance.save()
                change.attachment.add(file_instance)
            messages.success(
                request, f'{change.change_name} added to {change.project_id}')

        else:
            if form.is_valid() is False:
                messages.error(request, mark_safe(
                    f'There was an error submitting the change.<br>Try again.'))
            elif attachmentForm.is_valid() is False:
                messages.error(request, mark_safe(
                    f'There was an error attaching the document(s) to the change.<br>Try again to add the change.'))
            else:
                messages.error(request, mark_safe(
                    f'There was an error submitting the change.<br>Try again.'))

        return redirect(reverse('get_dashboard', args=[project.id]))

    return redirect(reverse('get_dashboard', args=[project.id]))


@login_required
def edit_change(request, change_id):
    """
    Edit a change on the List of Changes
    """
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
            messages.success(
                request, f'{change.change_name} has been updated')

        else:
            messages.error(request, mark_safe(
                f'There was an error updating the change.<br>Try again.'))

        return redirect(reverse('get_dashboard', args=[change.project_id_id]))

    else:
        project = Project.objects.get(pk=change.project_id_id)

        # required to determine permission of user, if not a project user then project owner
        try:
            project_user = ProjectUser.objects.get(
                project=change.project_id_id, project_user=request.user)
        except ProjectUser.DoesNotExist:
            project_user = None

        changeForm = ChangeForm(instance=change)
        attachmentsForm = ChangeAttachmentsForm(instance=change)
        attachments = change.attachment.all()
        template = 'dashboard/edit_change.html'

        context = {
            'project': project,
            'project_user': project_user,
            'changeForm': changeForm,
            'attachmentsForm': attachmentsForm,
            'change': change,
            'attachments': attachments,
        }

        return render(request, template, context)


@login_required
def delete_file(request, change_id, file_id):
    """
    Delete an attachment a Change whilst in the Edit Change mode
    """

    attachment = get_object_or_404(ChangeAttachments, pk=file_id)
    attachment.delete()

    return redirect(reverse('edit_change', args=[change_id]))


@login_required
def delete_change(request, change_id):
    """
    Delete a Change from the List of Changes
    """

    change = get_object_or_404(Change, pk=change_id)

    # Step to delete all attachments and files stored, not just the database entry
    attachments = change.attachment.all()
    for a in attachments:
        a.delete()

    change.delete()

    return redirect(reverse('get_dashboard', args=[change.project_id_id]))
