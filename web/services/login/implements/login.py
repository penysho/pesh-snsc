import logging

from django.contrib.auth.forms import AuthenticationForm

from web.components.common.session import SnscSession
from web.models import Site
from web.repositories.site.site import SiteRepository
from web.services.exceptions import SitePermissionException
from web.services.login.login import LoginService

logger = logging.getLogger(__name__)


class LoginServiceImpl(LoginService):

    def __init__(self, session: SnscSession, site_repository: SiteRepository) -> None:
        self.session = session
        self.site_repository = site_repository

    def create_site(self, form: AuthenticationForm) -> Site:
        site = self.site_repository.fetch_sites().first()
        if site is None:
            logger.error(
                f"ユーザー {form.get_user().id}: 操作権限を持つサイトがありません"
            )
            raise SitePermissionException()
        else:
            self.session.create_current_site(site)
            return site
