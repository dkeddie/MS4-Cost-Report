from django.contrib import admin
from .models import Project, Change, ProjectUser, ChangeAttachments

# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectUser)
admin.site.register(Change)
admin.site.register(ChangeAttachments)