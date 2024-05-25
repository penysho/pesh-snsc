from django.core.exceptions import ObjectDoesNotExist
from django.db.models.manager import BaseManager

from web.models import Sns, SnsUserAccount
from web.repositories.exceptions import DatabaseException, NotFoundObjectException
from web.repositories.sns.sns_user_account import SnsUserAccountRepository


class SnsUserAccountRepositoryImpl(SnsUserAccountRepository):

    def fetch_sns_user_account_by_type(self, site_id: int, type: str) -> SnsUserAccount:
        try:
            return SnsUserAccount.objects.select_related("sns").get(
                is_active=True,
                sns__site_id=site_id,
                sns__type=type,
                sns__is_active=True,
            )
        except ObjectDoesNotExist:
            raise NotFoundObjectException(
                SnsUserAccount,
                f"SnsUserAccount with site id {site_id} and type {type} not found",
            )
        except Exception as e:
            raise DatabaseException(e)

    def fetch_sns_user_accounts(self, site_id: int) -> BaseManager[SnsUserAccount]:
        return SnsUserAccount.objects.select_related("sns").filter(
            is_active=True, sns__site_id=site_id, sns__is_active=True
        )

    def update_or_create_by_response(
        self, sns: Sns, response: dict[str, int]
    ) -> tuple[SnsUserAccount, bool]:
        sns_user_account, created = SnsUserAccount.objects.update_or_create(
            sns=sns,
            defaults={**response},
            create_defaults={"sns": sns, "is_active": True, **response},
        )
        return sns_user_account, created
