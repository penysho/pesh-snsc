from django.core.exceptions import ObjectDoesNotExist
from django.db.models.manager import BaseManager

from web.models import Site
from web.repositories.exceptions.exceptions import DatabaseException, NotFoundException
from web.repositories.site.site import SiteRepository


class SiteRepositoryImpl(SiteRepository):

    def __init__(self, email: str):
        self.email = email

    def fetch_site_by_id(self, id: int) -> Site:
        try:
            return Site.objects.get(
                is_active=True, id=id, siteownership__snsc_user__email=self.email
            )
        except ObjectDoesNotExist:
            raise NotFoundException(Site, f"Site with id {id} not found")
        except Exception as e:
            raise DatabaseException(e)

    def fetch_site_by_name(self, name: str) -> Site:
        try:
            return Site.objects.get(
                is_active=True, name=name, siteownership__snsc_user__email=self.email
            )
        except ObjectDoesNotExist:
            raise NotFoundException(Site, f"Site with name {name} not found")
        except Exception as e:
            raise DatabaseException(e)

    def fetch_sites(self) -> BaseManager[Site]:
        return Site.objects.filter(
            is_active=True, siteownership__snsc_user__email=self.email
        )
