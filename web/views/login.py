from django.contrib.auth.views import LoginView as BaseLoginView

from web.components.common.template import get_template_name
from web.forms import LoginFrom
from web.handlers.login import LoginHandler


class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = get_template_name("login.html")

    def form_valid(self, form):
        handler = LoginHandler()
        handler.save_session(request=self.request, form=form)
        return super().form_valid(form)
