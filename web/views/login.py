import logging

from django.contrib.auth.views import LoginView as BaseLoginView

from web.components.common.template import get_template_name
from web.forms import LoginFrom
from web.handlers.login import LoginHandler

logger = logging.getLogger(__name__)


class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = get_template_name("login.html")

    def form_valid(self, form):
        login_handler = LoginHandler()
        site = login_handler.create_site(request=self.request, form=form)
        logger.info(f"ユーザー: {form.get_user().id}: {site.name}にログインしました")
        return super().form_valid(form)
