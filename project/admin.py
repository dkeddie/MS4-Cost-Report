from django.contrib import admin

from .models import Project, ProjectUser

# Register your models here.

class ProjectUserInline(admin.TabularInline):
  model = ProjectUser

class ProjectAdmin(admin.ModelAdmin):
  inlines = [
    ProjectUserInline
  ]

admin.site.register(Project, ProjectAdmin)

