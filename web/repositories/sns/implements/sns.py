from django.db.models.manager import BaseManager

from web.models import Sns
from web.repositories.sns.sns import SnsRepository


class SnsRepositoryImpl(SnsRepository):

    def fetch_sns_by_type(self, site_id: int, type: str) -> Sns:
        return Sns.objects.get(
            site_id=site_id,
            type=type,
            is_active=True,
        )

    def fetch_sns_list(self, site_id: int) -> BaseManager[Sns]:
        return Sns.objects.filter(
            site_id=site_id,
            is_active=True,
        )
