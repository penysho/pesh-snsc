import logging

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest

from web.components.common.session import SnscSession
from web.models import Site
from web.repositories.site.implements.site import SiteRepositoryImpl
from web.services.index.index import IndexService

logger = logging.getLogger(__name__)


class IndexServiceImpl(IndexService):

    def __init__(self, request: HttpRequest) -> None:
        self.request = request

    def change_site(self) -> Site | None:
        try:
            change_site = self.request.POST.get("site")
            site_repository = SiteRepositoryImpl(email=self.request.user.email)
            site = site_repository.fetch_site_by_name(name=change_site)

            session = SnscSession(self.request.session)
            session.create_current_site(site)
            return site
        except ObjectDoesNotExist as e:
            logger.error(
                f"ユーザー {self.request.user.id}: {site.name}の権限がありません"
            )
            raise e
