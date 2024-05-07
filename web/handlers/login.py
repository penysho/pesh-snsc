from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest

from web.components.common.session import SnscSession
from web.models import Site
from web.sevices.site import SiteService


class LoginHandler:

    def create_site(
        self, request: HttpRequest, form: AuthenticationForm
    ) -> Site | None:
        site_service = SiteService(email=form.get_user())
        site = site_service.fetch_sites().first()
        session = SnscSession(request.session)
        session.create_current_site(site)
        return site
