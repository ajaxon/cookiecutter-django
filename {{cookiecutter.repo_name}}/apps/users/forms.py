from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms


class MySignUpForm(forms.Form):
    terms = forms.BooleanField(required=False,label='Acceptance of terms and conditions',help_text='I am 18 or over')

    def __init__(self, *args, **kwargs):
        super(MySignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Register',
                'username',
                'email',
                'password1',
                'password2',
                'terms'
            ),
            ButtonHolder(
                Submit('register', 'Register', css_class='btn btn-primary')
            )
        )

    def clean_terms(self):
        terms = self.cleaned_data['terms']
        if not terms:
            raise forms.ValidationError("You must accept the terms")
        return terms
    def signup(self, request, user):
        user.terms = self.cleaned_data['terms']
        user.save()
