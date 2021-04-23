from django.contrib import admin

from .models import Project, ProjectUser

# Register your models here.

admin.site.register(Project)

@admin.register(ProjectUser)
class ProjectUserAdmin(admin.ModelAdmin):
  list_display = ("project_user", "project", "user_permission")