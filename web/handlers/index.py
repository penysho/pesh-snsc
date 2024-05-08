import logging

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest

from web.components.common.session import SnscSession
from web.models import Site
from web.sevices.site import SiteService

logger = logging.getLogger(__name__)


class IndexHandler:

    def change_site(self, request: HttpRequest) -> Site | None:
        try:
            change_site = request.POST.get("site")
            site_service = SiteService(email=request.user.email)
            site = site_service.fetch_site_by_name(name=change_site)

            session = SnscSession(request.session)
            session.create_current_site(site)
            return site
        except ObjectDoesNotExist as e:
            logger.error(f"ユーザー {request.user.id}: {site.name}の権限がありません")
            raise e