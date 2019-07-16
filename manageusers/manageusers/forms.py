from django import forms
from django.forms.widgets import ChoiceWidget

import account.forms
from django.urls import reverse


class SignupForm(account.forms.SignupForm):
    terms_agreement = forms.BooleanField()

    def __init__(self, **kwargs):
        super(SignupForm, self).__init__(**kwargs)
        self.fields['terms_agreement'].label = 'Você precisa ler e aceitar os <a href="%s" target="_blank">  termos and condições.</a>' % reverse('get_terms')

