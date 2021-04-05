from django import forms
from django.forms import ClearableFileInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div

from .models import Project, ProjectUser, Change, ChangeAttachments
from profile.models import UserSubDetails


class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['project_name', 'original_estimate']


class UserSubDetailsForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):

        super(UserSubDetailsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
          Div(
            Div('default_street_address1', css_class='col-6',),
            Div('default_street_address2', css_class='col-6',),
            Div('default_town_or_city', css_class='col-6',),
            Div('default_county', css_class='col-6',),
            Div('default_postcode', css_class='col-6',),
            Div('default_country', css_class='col-6',),
            Div('default_phone_number', css_class='col-6',),
            css_class='row'
          )
        )

  class Meta:
    model = UserSubDetails
    fields = ['default_phone_number', 'default_street_address1','default_street_address2', 'default_town_or_city', 'default_county', 'default_postcode', 'default_country']


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

    
class ChangeAttachmentsForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):

      super(ChangeAttachmentsForm, self).__init__(*args, **kwargs)
      self.helper = FormHelper(self)
      self.helper.form_tag = False
      self.helper.disable_csrf = True
      self.helper.layout = Layout(
        Div(
          Div('attachment', css_class="col-12",),
          css_class='row'
        ),
      )

  class Meta:
    model = ChangeAttachments
    fields = ['attachment']
    widgets = {
            'attachment': ClearableFileInput(attrs={'multiple': True}),
        }
