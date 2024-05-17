from requests import Response

from web.models.sns_api_account import SnsApiAccount
from web.repositories.api.api import ApiRepository


class TiktokRepositoryImpl(ApiRepository):

    def fecth_user(self, sns_api_account: SnsApiAccount) -> dict:
        pass

    def fecth_media(self, sns_api_account: SnsApiAccount) -> dict:
        pass

    def create_get_media_url(self, sns_api_account: SnsApiAccount) -> str:
        pass

    def create_get_user_url(self, sns_api_account: SnsApiAccount) -> str:
        pass

    def convert_get_media_for_register(self, response: Response) -> dict:
        pass

    def convert_get_user_for_register(self, response: Response) -> dict:
        pass
