from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

from payments.models import ProjectStripeDetails


class UserProfile(models.Model):
  """User profile with extended information from  registration"""

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  company = models.CharField(max_length=40, null=False, blank=True)

  def __str__(self):
    return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
  """Create or update the user profile"""
  if created:
    UserProfile.objects.create(user=instance)
  # Existing users: just save the profile
  instance.userprofile.save()


class UserSubscriptionDetails(models.Model):
    """
    A user profile model for subscription details information
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscriptions =  models.ManyToManyField(ProjectStripeDetails)
    default_phone_number = models.CharField("Phone Number", max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField("Street Address 1", max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField("Street Address 2", max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField("Town/City", max_length=40, null=True, blank=True)
    default_county = models.CharField("County", max_length=80, null=True, blank=True)
    default_postcode = models.CharField("Post Cost", max_length=20, null=True, blank=True)
    default_country = CountryField("Country", blank_label="Country", null=True, blank=True)

    def __str__(self):
        return self.user.username