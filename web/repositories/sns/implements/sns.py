from django.db.models.manager import BaseManager

from web.models import Sns
from web.repositories.sns.sns import SnsRepository


class SnsRepositoryImpl(SnsRepository):

    def __init__(self, site_id: str):
        self.site_id = site_id

    def fetch_sns_by_type(self, type: str) -> Sns:
        return Sns.objects.get(
            site_id=self.site_id,
            type=type,
            is_active=True,
        )

    def fetch_sns_list(self) -> BaseManager:
        return Sns.objects.filter(
            site_id=self.site_id,
            is_active=True,
        )
