from django.contrib import admin
from .models import Project, Change, ProjectUser, Project_StripeDetails, ChangeAttachments

# Register your models here.

admin.site.register(Project)
admin.site.register(Project_StripeDetails)
admin.site.register(ProjectUser)
admin.site.register(Change)
admin.site.register(ChangeAttachments)