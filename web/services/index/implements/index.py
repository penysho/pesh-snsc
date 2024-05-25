import logging

from django.http import HttpRequest

from core.session.session import SnscSession
from web.models import Site
from web.repositories.exceptions import NotFoundObjectException
from web.repositories.site.site import SiteRepository
from web.services.exceptions import SitePermissionException
from web.services.index.index import IndexService

logger = logging.getLogger(__name__)


class IndexServiceImpl(IndexService):

    def __init__(self, session: SnscSession, site_repository: SiteRepository) -> None:
        self.session = session
        self.site_repository = site_repository

    def change_site(self, request: HttpRequest) -> Site:
        try:
            change_site = self.request.POST.get("site")
            site = self.site_repository.fetch_site_by_name(
                email=request.user.email, name=change_site
            )
            self.session.create_current_site(site)
            return site
        except NotFoundObjectException:
            logger.error(
                f"ユーザー {self.request.user.id}: {site.name}の権限がありません"
            )
            raise SitePermissionException()
