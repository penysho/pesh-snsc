from django.core.exceptions import ObjectDoesNotExist
from django.db.models.manager import BaseManager

from web.models import Site
from web.repositories.exceptions import DatabaseException, NotFoundObjectException
from web.repositories.site.site import SiteRepository


class SiteRepositoryImpl(SiteRepository):
    def fetch_site_by_id(self, id: int) -> Site:
        try:
            return Site.objects.get(is_active=True, id=id)
        except ObjectDoesNotExist:
            raise NotFoundObjectException(Site, f"Site with id {id} not found")
        except Exception as e:
            raise DatabaseException(e)

    def fetch_site_by_name(self, email: str, name: str) -> Site:
        try:
            return Site.objects.get(
                is_active=True, name=name, siteownership__snsc_user__email=email
            )
        except ObjectDoesNotExist:
            raise NotFoundObjectException(Site, f"Site with name {name} not found")
        except Exception as e:
            raise DatabaseException(e)

    def fetch_sites(
        self,
        email: str,
    ) -> BaseManager[Site]:
        return Site.objects.filter(
            is_active=True, siteownership__snsc_user__email=email
        )
