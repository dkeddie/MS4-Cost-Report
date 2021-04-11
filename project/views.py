from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages


from .models import Project, ProjectUser, User
from payments.models import ProjectStripeDetails
from .forms import ProjectForm, ProjectUserForm


def project_admin(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    projectForm = ProjectForm()
    userForm = ProjectUserForm()
    users = ProjectUser.objects.filter(project_id=project_id)
    stripeUser = get_object_or_404(ProjectStripeDetails, project=project)

    template = 'project/admin.html'
    context = {
        'project': project,
        'projectForm': projectForm,
        'userForm': userForm,
        'users': users,
        'stripeUser': stripeUser.stripe_customer_id,
    }

    return render(request, template, context)


def add_user(request, project_id):

    if request.method == 'POST':
        form = ProjectUserForm(request.POST)
        project = get_object_or_404(Project, pk=project_id)

        try:
            user_id = User.objects.get(email=form.data['email'])
        except User.DoesNotExist:
            user_id = None

        if form.is_valid():
            if ProjectUser.objects.filter(project_user_id=user_id.id).exists():
                messages.success(request, f'User already exists')
            elif user_id is not None:
                projectuser = form.save(commit=False)
                projectuser.project = project
                projectuser.project_user_id = user_id.id
                projectuser.save()
                messages.success(request, f'User invited to the Project')
            else:
                messages.success(request, f'Not registered')
        else:
            print("no")

        return redirect(reverse('project_admin', args=[project.id]))


def delete_user(request, project_user_id):
    projectuser = get_object_or_404(
        ProjectUser, project_user_id=project_user_id)

    projectuser.delete()

    messages.success(
        request, f'{projectuser.project_user} deleted and will no longer have access to the Project')

    return redirect(reverse('project_admin', args=[projectuser.project_id]))
