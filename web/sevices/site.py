from django.db.models.manager import BaseManager

from web.models import Site


class SiteService:

    def fetch_sites(self, email: str) -> BaseManager[Site]:
        return Site.objects.filter(
            is_active=True, siteownership__snsc_user__email=email
        )
