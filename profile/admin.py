from django.contrib import admin
from .models import UserProfile, UserSubscriptionDetails


# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserSubscriptionDetails)
