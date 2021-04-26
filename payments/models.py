from django.db import models
from django.contrib.auth.models import User

from django.conf import settings

from project.models import Project

import os


class ProjectStripeDetails(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  customer_id = models.CharField(max_length=20, null=False, blank=False)
  stripe_sub = models.CharField(max_length=40, null=False, blank=False)

  def __str__(self):
    return self.project.project_name

  def sub_status(self):
    import stripe
    stripe.api_key = settings.STRIPE_SECRET_KEY
    sub = stripe.Subscription.retrieve(self.stripe_sub)
    return sub.status

  class Meta:
    verbose_name = "Stripe Details"
    verbose_name_plural = "Stripe Details"

