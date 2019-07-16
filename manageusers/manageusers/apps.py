from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "manageusers"

    def ready(self):
        import_module("manageusers.receivers")
