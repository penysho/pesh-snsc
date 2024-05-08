import logging

from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.http import HttpRequest

from web.components.common.session import SnscSession
from web.models import Site
from web.sevices.site import SiteService

logger = logging.getLogger(__name__)


class LoginHandler:

    def create_site(self, request: HttpRequest, form: AuthenticationForm) -> Site:
        site_service = SiteService(email=form.get_user())
        site = site_service.fetch_sites().first()
        if site is None:
            logger.error(
                f"ユーザー {form.get_user().id}: 操作権限を持つサイトがありません"
            )
            raise ValidationError("操作権限を持つサイトがありません")
        else:
            session = SnscSession(request.session)
            session.create_current_site(site)
            return site
