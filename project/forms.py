from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from .models import Project, ProjectUser


class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div('project_name', css_class="col-12",),
                Div('original_estimate', css_class="col-12",),
                css_class='row'
            )
        )

    class Meta:
        model = Project
        fields = ['project_name', 'original_estimate']


class ProjectUserForm(forms.ModelForm):
    email = forms.CharField(label='Email', max_length=50)

    def __init__(self, *args, **kwargs):

        super(ProjectUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div('email', css_class="col-12",),
                css_class='row'
            ),
            Div(
                Div('user_permission', css_class="col-4",),
                css_class='row'
            )
        )

    class Meta:
        model = ProjectUser
        fields = ['email', 'user_permission']
