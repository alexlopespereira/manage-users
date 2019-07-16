import account.views
from django.db import models
from django.conf import settings
from .forms import SignupForm


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birthdate = models.DateField()


def update_profile(self, form):
    UserProfile.objects.create(
        user=self.created_user
    )


def after_signup(self, form):
    self.update_profile(form)
    super(SignupView, self).after_signup(form)


class SignupView(account.views.SignupView):
    pass


class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm
