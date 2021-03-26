from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from .models import Project, ProjectUser, Change


class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['project_name', 'original_estimate']


class ChangeForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):

        super(ChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
          Div(
            Div('change_name', css_class="col-12",),
            css_class='row'
          ),
          Div(
            Div('change_status', css_class='col-6',),
            Div('change_cost', css_class='col-6',),
            css_class='row'
          )
        )
  
  class Meta:
    model = Change
    fields = ['change_name', 'change_status', 'change_cost']

    

