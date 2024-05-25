from django.core.exceptions import ObjectDoesNotExist
from django.db.models.manager import BaseManager

from web.models import Sns
from web.repositories.exceptions import DatabaseException, NotFoundObjectException
from web.repositories.sns.sns import SnsRepository


class SnsRepositoryImpl(SnsRepository):

    def fetch_sns_by_type(self, site_id: int, type: str) -> Sns:
        try:
            return Sns.objects.get(
                site_id=site_id,
                type=type,
                is_active=True,
            )
        except ObjectDoesNotExist:
            raise NotFoundObjectException(
                Sns,
                f"Sns with site id {site_id} and type {type} not found",
            )
        except Exception as e:
            raise DatabaseException(e)

    def fetch_sns_list(self, site_id: int) -> BaseManager[Sns]:
        return Sns.objects.filter(
            site_id=site_id,
            is_active=True,
        )
