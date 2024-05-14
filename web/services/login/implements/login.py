import logging

from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.http import HttpRequest

from web.components.common.session import SnscSession
from web.models import Site
from web.repositories.site.implements.site import SiteRepositoryImpl
from web.services.login.login import LoginService

logger = logging.getLogger(__name__)


class LoginServiceImpl(LoginService):

    def __init__(self, request: HttpRequest) -> None:
        self.request = request

    def create_site(self, form: AuthenticationForm) -> Site:
        site_repository = SiteRepositoryImpl(email=form.get_user())
        site = site_repository.fetch_sites().first()
        if site is None:
            logger.error(
                f"ユーザー {form.get_user().id}: 操作権限を持つサイトがありません"
            )
            raise ValidationError("操作権限を持つサイトがありません")
        else:
            session = SnscSession(self.request.session)
            session.create_current_site(site)
            return site
