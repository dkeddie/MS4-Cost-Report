from django.contrib import admin

from .models import Project, ProjectUser

# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectUser)
