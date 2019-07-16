from django.conf import settings
from django.conf.urls import url

from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView

from django.contrib import admin
from .views import SignupView, LoginView, get_terms

urlpatterns = [
    path("", TemplateView.as_view(template_name="homepage.html"), name="home"),
    path("admin/", admin.site.urls),
    url(r"^account/signup/$", SignupView.as_view(), name="account_signup"),
    url(r"^account/login/$", LoginView.as_view(), name="account_login"),
    url(r"^terms/$", get_terms, name="get_terms"),
    path("account/", include("account.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
