import logging

from django.contrib.auth.views import LoginView as BaseLoginView

from web.components.common.session import SnscSession
from web.components.common.template import get_template_name
from web.forms import LoginFrom
from web.repositories.site.implements.site import SiteRepositoryImpl
from web.services.login.implements.login import LoginServiceImpl

logger = logging.getLogger(__name__)


class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = get_template_name("login.html")

    def form_valid(self, form):
        service = LoginServiceImpl(
            rsession=SnscSession(self.request.session),
            site_repository=SiteRepositoryImpl(),
        )
        site = service.create_site(form=form)
        logger.info(f"ユーザー {form.get_user().id}: {site.name}にログインしました")
        return super().form_valid(form)
