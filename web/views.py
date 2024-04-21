from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views import generic

from web.apps import WebConfig

from .forms import LoginFrom


def get_template_name(file_name: str) -> str:
    return f"{WebConfig.name}/{file_name}"


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = get_template_name("index.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = get_template_name("login.html")


class LogoutView(LoginRequiredMixin, BaseLogoutView):
    template_name = get_template_name("login.html")
