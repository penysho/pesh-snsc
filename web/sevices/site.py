from django.db.models.manager import BaseManager

from web.models import Site


class SiteService:

    def __init__(self, email: str):
        self.email = email

    def fetch_sites(self) -> BaseManager[Site]:
        return Site.objects.filter(
            is_active=True, siteownership__snsc_user__email=self.email
        )

    def fetch_site_by_name(self, name: str) -> Site:
        return Site.objects.get(
            is_active=True, name=name, siteownership__snsc_user__email=self.email
        )
