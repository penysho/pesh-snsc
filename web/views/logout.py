from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView as BaseLogoutView

from web.components.common.template import get_template_name


class LogoutView(LoginRequiredMixin, BaseLogoutView):
    template_name = get_template_name("login.html")
