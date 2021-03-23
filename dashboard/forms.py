from django import forms
from .models import Project, ProjectUser


class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['project_name', 'original_estimate']

