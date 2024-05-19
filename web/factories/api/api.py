from web.models import Sns, SnsApiAccount
from web.repositories.api.implements.instagram import InstagramRepositoryImpl
from web.repositories.api.implements.tiktok import TiktokRepositoryImpl


class ApiFactory:

    def __init__(
        self,
        instagram_repository: InstagramRepositoryImpl,
        tiktok_repository: TiktokRepositoryImpl,
    ):
        self.instagram_repository = instagram_repository
        self.tiktok_repository = tiktok_repository

    def get_repository_by_type(self, type: str):
        if type == Sns.SnsType.INSTAGRAM:
            return self.instagram_repository
        elif type == Sns.SnsType.TIKTOK:
            return self.tiktok_repository
        else:
            raise ValueError("Unsupported SNS type")

    def get_repository_by_sns_api_account(self, sns_api_account: SnsApiAccount):
        if sns_api_account.sns.type == Sns.SnsType.INSTAGRAM:
            return self.instagram_repository
        elif sns_api_account.sns.type == Sns.SnsType.TIKTOK:
            return self.tiktok_repository
        else:
            raise ValueError("Unsupported SNS type")
