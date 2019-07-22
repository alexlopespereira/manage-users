import account.views
from account.models import SignupCode
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import SignupForm
from django.http import request, Http404
from account.compat import is_authenticated


class SignupView(account.views.SignupView):
    form_class = SignupForm

    def post(self, *args, **kwargs):
        if is_authenticated(self.request.user):
            raise Http404()
        try:
            validate_password(password=args[0].POST['password'])
        except ValidationError as e:
            form = SignupForm()
            form.username = args[0].POST['username']
            form.email = args[0].POST['email']
            messages.warning(self.request, 'A senha informada não atende aos requisitos mínimos. Tente uma outra senha.')
            # return render(self.request, 'account/signup.html', {'form': form})
            return redirect(reverse('account_signup'))
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
