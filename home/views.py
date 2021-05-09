from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User
from allauth.account.models import EmailAddress

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

    # UPDATE USER PROFILE DETAILS DIRECT ON THE INDEX PAGE
    if request.POST:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        company = request.POST.get('company')

        if user.email != email:
            try:
                update = User.objects.get(email=email)
                messages.error(request, f'{email} already registered to another user')
            except User.DoesNotExist:
                # Update User model
                update = User.objects.get(pk=user.id)
                update.email = email
                update.first_name= firstname
                update.last_name = lastname
                update.save()
                # Update EmailAddress model so that emails match
                newemail = EmailAddress.objects.get(email=user.email)
                newemail.email = email
                newemail.save()

                obj, created = UserProfile.objects.update_or_create(
                user=user,
                defaults={'company': company},
                )

                messages.success(request, f'User Profile updated')
        else:
            # Update User model
            update = User.objects.get(pk=user.id)
            update.email = email
            update.first_name= firstname
            update.last_name = lastname
            update.save()
            #Update EmailAddress model so that emails match
            newemail = EmailAddress.objects.get(email=user.email)
            newemail.email = email
            newemail.save()

            obj, created = UserProfile.objects.update_or_create(
                user=user,
                defaults={'company': company},
            )

            messages.success(request, f'User Profile updated')

        return redirect('home')

    else:
        registration = user
        profile = get_object_or_404(UserProfile, user=user)
        form = ProjectForm()
        subForm = UserSubscriptionDetailsForm()

        # GENERATE LIST OF PROJECTS ACCESSIBLE BY USER
        # Step 1 - List where user is Project Owner
        projects = Project.objects.filter(
            project_owner_id=user.id)
        # Add projects to List where user is a Project User
        u = get_object_or_404(User, pk=request.user.id)
        otherprojects = u.p_users.all()  # generates list where project user
        for other in otherprojects:
            projects |= Project.objects.filter(
                id=other.id)  # merges second list into first

        # UPDATE SUBSCRIPTION STATUS OF EACH PROJECT TO BE DISPLAYED
        for project in projects:
            try:
                project_sub = ProjectStripeDetails.objects.get(
                    project=project.id)
            except ObjectDoesNotExist:
                project_sub = None

            if project_sub is not None:
                subActive = ProjectStripeDetails.sub_status(project_sub)
                if subActive == 'active':
                    Project.objects.filter(pk=project.id).update(
                        has_subscription=True)
                else:
                    Project.objects.filter(pk=project.id).update(
                        has_subscription=False)

            else:
                Project.objects.filter(pk=project.id).update(
                    has_subscription=False)

        template = 'home/index.html'
        context = {
            'registration': registration,
            'profile': profile,
            'form': form,
            'subForm': subForm,
            'projects': projects,
        }
        return render(request, template, context)

    return redirect('/accounts/login/')
