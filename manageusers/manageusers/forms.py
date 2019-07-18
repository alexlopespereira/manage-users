from django import forms
import account.forms


class SignupForm(account.forms.SignupForm):
    terms_agreement = forms.BooleanField()

    def __init__(self, **kwargs):
        super(SignupForm, self).__init__(**kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'readonly': 'readonly'})
