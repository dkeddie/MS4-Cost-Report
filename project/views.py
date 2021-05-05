from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.utils.safestring import mark_safe

from django.core.mail import send_mail
from django.template.loader import render_to_string


from .models import Project, ProjectUser, User
from .forms import ProjectForm, ProjectUserForm

from payments.models import ProjectStripeDetails

from profile.models import UserSubscriptionDetails
from profile.forms import UserSubscriptionDetailsForm


def create_project(request):
    """New Project"""
    subForm = UserSubscriptionDetailsForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.project_owner = request.user
            project.save()
            messages.success(request, f'{project.project_name} created')

        return redirect(reverse(subscribe, args=[project.id]))


def subscribe(request, project_id):
    """Initiate new subscription and payment process"""
    user = get_object_or_404(User, id=request.user.id)
    project = get_object_or_404(Project, id=project_id)
    subForm = UserSubscriptionDetailsForm()

    template = 'payments/payment-method.html'
    context = {
        'user': user,
        'project': project,
        'form': subForm,
    }

    return render(request, template, context)


def project_admin(request, project_id):
    """View Project Admin Page"""
    project = Project.objects.get(id=project_id)

    # Update details displayed on the page
    if request.POST:
        pname = request.POST.get("project_name")
        est = request.POST.get("original_estimate")
        est_strip = est.replace('£', '').replace(',', '').strip()
        Project.objects.filter(pk=project_id).update(
            project_name=pname, original_estimate=est_strip)

        return redirect(reverse(project_admin, args=[project_id]))

    # Displays Project Details and Lists of Users with access to the project
    else:
        projectForm = ProjectForm()
        userForm = ProjectUserForm()
        users = ProjectUser.objects.filter(project=project)
        stripeUser = get_object_or_404(ProjectStripeDetails, project=project)

        template = 'project/admin.html'
        context = {
            'project': project,
            'projectForm': projectForm,
            'userForm': userForm,
            'users': users,
            'stripeUser': stripeUser.customer_id,
        }

    return render(request, template, context)


def add_user(request, project_id):
    """Add user to the Project in Project Admin page"""
    if request.method == 'POST':
        form = ProjectUserForm(request.POST)
        project = get_object_or_404(Project, pk=project_id)
        email = request.POST.get('email')

        try:
            user_id = User.objects.get(email=form.data['email'])
        except User.DoesNotExist:
            user_id = None

        if form.is_valid():
            if user_id is not None:
                if ProjectUser.objects.filter(
                    project_user=user_id.id).filter(
                        project=project).exists():
                    messages.success(
                        request, f'User already has access to this Project')
                else:
                    projectuser = form.save(commit=False)
                    projectuser.project_user = user_id
                    projectuser.project = project
                    projectuser.save()
                    project.project_users.add(projectuser.project_user)
                    messages.success(request, f'User invited to the Project')
            else:

                context = {
                    'user': request.user,
                    'project': project
                }

                subject = 'You are invited to use Cost Report'
                plain_message = render_to_string(
                    'project/emails/invitation.txt', context)
                from_email = 'Cost Report'
                to = email
                html_message = render_to_string(
                    'project/emails/invitation.html', context)

                send_mail(
                        subject,
                        plain_message,
                        from_email,
                        [to],
                        fail_silently=False,
                        html_message=html_message
                        )

                messages.success(request, mark_safe(
                    f'{email} is not a registered user.<br><br>'
                    f'An email has been issued inviting them to join.<br><br>'
                    f'You will need to invite them again once they register.'))
        else:
            messages.error(
                request, f'An invalid entry was submitted. Please try again')

        return redirect(reverse('project_admin', args=[project.id]))


def delete_user(request, project_id, project_user_id):
    """Delete user from the Project"""
    projectuser = get_object_or_404(
        ProjectUser, project_user=project_user_id)

    projectuser.delete()

    messages.success(
        request, f'{projectuser.project_user} '
        f'deleted and will no longer have access to the Project')

    return redirect(reverse('project_admin', args=[project_id]))
