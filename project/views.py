from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages


from .models import Project, ProjectUser, User
from .forms import ProjectForm, ProjectUserForm

from payments.models import ProjectStripeDetails

from profile.models import UserSubscriptionDetails
from profile.forms import UserSubscriptionDetailsForm


def create_project(request):

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

    user = get_object_or_404(User, id=request.user.id)
    project = get_object_or_404(Project, id=project_id)
    subForm = UserSubscriptionDetailsForm()

    template = 'payments/payment-method.html'
    context = {
        'user': user,
        'project': project,
        'form':subForm,
    }

    return render(request, template, context)


def project_admin(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.POST:
        pname = request.POST.get("project_name")
        est = request.POST.get("original_estimate")
        est_strip = est.replace('£','').replace(',','').strip()
        Project.objects.filter(pk=project_id).update(project_name=pname, original_estimate=est_strip)

        return redirect(reverse(project_admin, args=[project_id]))

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

    if request.method == 'POST':
        form = ProjectUserForm(request.POST)
        project = get_object_or_404(Project, pk=project_id)

        try:
            user_id = User.objects.get(email=form.data['email'])
        except User.DoesNotExist:
            user_id = None

        if form.is_valid():
            if ProjectUser.objects.filter(project_user=user_id.id).filter(project=project).exists():
                messages.success(request, f'User already exists')
            elif user_id is not None:
                projectuser = form.save(commit=False)
                projectuser.project_user = user_id
                projectuser.project = project
                projectuser.save()
                print(user_id)
                project.project_users.add(projectuser.project_user)
                messages.success(request, f'User invited to the Project')
            else:
                messages.success(request, f'Not registered')
        else:
            print("no")

        return redirect(reverse('project_admin', args=[project.id]))


def delete_user(request, project_id, project_user_id):
    projectuser = get_object_or_404(
        ProjectUser, project_user=project_user_id)

    projectuser.delete()

    messages.success(
        request, f'{projectuser.project_user} deleted and will no longer have access to the Project')

    return redirect(reverse('project_admin', args=[project_id]))
