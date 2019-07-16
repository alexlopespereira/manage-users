import account.views
from django.shortcuts import render

from .models import UserProfile
from .forms import SignupForm
from django.http import request



class SignupView(account.views.SignupView):
    form_class = SignupForm

    def after_signup(self, form):
        self.update_profile(form)
        super(SignupView, self).after_signup(form)

    def update_profile(self, form):
        profile = self.created_user.profile  # replace with your reverse one-to-one profile attribute
        profile.terms_agreement = form.cleaned_data["terms_agreement"]
        profile.save()


class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm


def get_terms():

    return render(request, 'terms.html')
