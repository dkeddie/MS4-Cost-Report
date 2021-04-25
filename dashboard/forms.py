from django import forms
from django.forms import ClearableFileInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from crispy_forms.bootstrap import PrependedText

from .models import Change, ChangeAttachments
# from profile.models import UserSubDetails




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
            Div(PrependedText('change_cost', '£'), css_class='col-6',),
            css_class='row'
          )
        )
  
  class Meta:
    model = Change
    fields = ['change_name', 'change_status', 'change_cost']
    localized_fields = ('change_cost',)

    
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
