from django.db import models
from django.contrib.auth.models import User

from django.conf import settings

class Project(models.Model):
  project_name = models.CharField("Project Name", max_length=30, null=False, blank=False)
  project_owner = models.ForeignKey(User, on_delete=models.CASCADE)
  original_estimate = models.DecimalField("Estimate/Budget", default=0, max_digits=15, decimal_places=2, null=False, blank=False)
  has_subscription = models.BooleanField(default=False, blank=True, null=True)

  def __str__(self):
        return self.project_name


class Project_StripeDetails(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  stripe_sub = models.CharField(max_length=40, null=False, blank=False)

  def __str__(self):
    return self.stripe_sub

  def sub_status(self):
    import stripe
    stripe.api_key = settings.STRIPE_SECRET_KEY
    sub = stripe.Subscription.retrieve(self)
    return sub.status


class ProjectUser(models.Model):
  PERMISSIONS = (
    ('Edit', 'Edit'),
    ('View', 'View'),
  )
  project_user = models.ForeignKey(User, on_delete=models.CASCADE)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  user_permission = models.CharField(max_length=4, choices=PERMISSIONS, null=False, blank=False)

  def __str__(self):
        return self.project_user.username


class Change(models.Model):
  CHANGE_STATUS = (
    ('A', 'Accepted'),
    ('P', 'Pending'),
    ('WiP', 'Work in Progress'),
    ('R', 'Rejected'),
  )
  project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
  project_user = models.ForeignKey(User, on_delete=models.CASCADE)
  change_name = models.CharField("Change Name", max_length=50, null=False, blank=False)
  change_status = models.CharField("Change Status", max_length=20, choices=CHANGE_STATUS, null=False, blank=False)
  change_cost = models.DecimalField("Change Cost", default=0, max_digits=15, decimal_places=2, null=False, blank=False)

  def __str__(self):
        return self.change_name
