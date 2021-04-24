from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User
from profile.models import UserProfile
from profile.forms import UserSubscriptionDetailsForm

from project.models import Project, ProjectUser
from project.forms import ProjectForm

from payments.models import ProjectStripeDetails

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def index(request):
    """ A view to return the index page """
    user = request.user

    if request.POST:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        company = request.POST.get('company')

        update1 = User.objects.filter(pk=user.id)
        print(update1)
        update1.update(
            first_name=firstname, last_name=lastname, email=email)
        UserProfile.objects.filter(pk=user.id).update(company=company)

        return redirect('home')

    else:
        registration = user
        profile = get_object_or_404(UserProfile, user=user)
        form = ProjectForm()
        subForm = UserSubscriptionDetailsForm()
        projects = Project.objects.filter(project_owner_id=user.id)

        # project = get_object_or_404(Project, pk=1)
        u = get_object_or_404(User, pk=1)
        otherprojects = u.p_users.all()
        for other in otherprojects:
            projects |= Project.objects.filter(project_name=other)

        stripeProjects = ProjectStripeDetails.objects.filter(
            project__in=projects)

        for project in projects:

            try:
                project_sub = ProjectStripeDetails.objects.get(
                    project=project.id)
            except ObjectDoesNotExist:
                project_sub = None

            if project_sub is not None:
                subActive = ProjectStripeDetails.sub_status(project_sub)
                if subActive == 'active':
                    Project.objects.filter(pk=project.id).update(has_subscription=True)
                else:
                    Project.objects.filter(pk=project.id).update(has_subscription=False)

            else:
                Project.objects.filter(pk=project.id).update(has_subscription=False)

        template = 'home/index.html'
        context = {
            'registration': registration,
            'profile': profile,
            'form': form,
            'subForm': subForm,
            'projects': projects,
            # 'otherprojects': otherprojects,
            'stripeProjects': stripeProjects,
        }
        return render(request, template, context)

    return redirect('/accounts/login/')
