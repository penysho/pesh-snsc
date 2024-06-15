from django.core.exceptions import ObjectDoesNotExist
from django.db.models.manager import BaseManager

from web.dto.api import SnsUserAccountDto
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

    def update_or_create(
        self, sns: Sns, sns_user_account_dto: SnsUserAccountDto
    ) -> SnsUserAccount:
        sns_user_account, _ = SnsUserAccount.objects.update_or_create(
            sns=sns,
            defaults={**sns_user_account_dto.model_dump()},
            create_defaults={
                "sns": sns,
                **sns_user_account_dto.model_dump(),
            },
        )
        return sns_user_account
