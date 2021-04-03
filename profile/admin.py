from django.contrib import admin
from .models import UserProfile, UserSubDetails, UserStripeDetails


# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserSubDetails)
admin.site.register(UserStripeDetails)
