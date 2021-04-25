from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div

from allauth.account.forms import SignupForm

from .models import UserSubscriptionDetails


class CustomSignupForm(SignupForm):
  first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
  last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
  
  def signup(self, request, user):
    user.first_name = self.cleaned_data['first_name']
    user.last_name = self.cleaned_data['last_name']
    user.save()
    return user


class UserSubscriptionDetailsForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):

        super(UserSubscriptionDetailsForm, self).__init__(*args, **kwargs)
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
    model = UserSubscriptionDetails
    fields = ['default_phone_number', 'default_street_address1','default_street_address2', 'default_town_or_city', 'default_county', 'default_postcode', 'default_country']
