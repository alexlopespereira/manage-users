import account.views
from account.models import SignupCode
from django.contrib.auth.models import Group
from django.shortcuts import render

from .models import UserProfile
from .forms import SignupForm
from django.http import request, Http404
from account.compat import is_authenticated

class SignupView(account.views.SignupView):
    form_class = SignupForm

    def post(self, *args, **kwargs):
        if is_authenticated(self.request.user):
            raise Http404()
        return super(account.views.SignupView, self).post(*args, **kwargs)

    def after_signup(self, form):
        self.update_profile(form)
        super(SignupView, self).after_signup(form)

    def update_profile(self, form):
        profile = self.created_user.profile  # replace with your reverse one-to-one profile attribute
        profile.terms_agreement = form.cleaned_data["terms_agreement"]
        profile.save()
        code = SignupCode.objects.get(email=self.created_user.email).code
        group_name = code.split('-')[0]
        group = Group.objects.get(name=group_name)
        group.user_set.add(self.created_user)


class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm


def get_terms():

    return render(request, 'terms.html')
