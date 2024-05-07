from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest

from web.components.common.session import SnscSession
from web.models import Site
from web.sevices.site import SiteService


class LoginHandler:

    def save_session(self, request: HttpRequest, form: AuthenticationForm) -> Site:
        site_service = SiteService(email=form.get_user())
        sites = [i for i in site_service.fetch_sites()]
        session = SnscSession(request.session)
        session.create_current_site(sites[0])
        session.create_sites(sites)
        return sites[0]
