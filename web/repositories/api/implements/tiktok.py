from requests import Response

from web.dto.api import PostDto
from web.models.sns_api_account import SnsApiAccount
from web.repositories.api.api import ApiRepository


class TiktokRepositoryImpl(ApiRepository):

    def fetch_user(self, sns_api_account: SnsApiAccount) -> dict:
        pass

    def fetch_post(self, sns_api_account: SnsApiAccount) -> list[PostDto]:
        pass

    def create_fetch_user_url(self, sns_api_account: SnsApiAccount) -> str:
        pass

    def create_fetch_post_url(self, sns_api_account: SnsApiAccount) -> str:
        pass

    def convert_user_dto(self, response: Response) -> dict:
        pass

    def convert_post_dto(self, response: Response) -> list[PostDto]:
        pass
