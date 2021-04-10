from django.db import models
from django.contrib.auth.models import User

from django.conf import settings

from dashboard.models import Project

import os


class ProjectStripeDetails(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  stripe_sub = models.CharField(max_length=40, null=False, blank=False)

  def __str__(self):
    return self.stripe_sub

  def sub_status(self):
    import stripe
    stripe.api_key = settings.STRIPE_SECRET_KEY
    sub = stripe.Subscription.retrieve(self)
    return sub.status

