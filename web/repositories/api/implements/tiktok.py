from requests import Response

from web.dto.api import PostDto, SnsUserAccountDto
from web.models.sns_api_account import SnsApiAccount
from web.repositories.api.api import ApiRepository


class TiktokRepositoryImpl(ApiRepository):

    def fetch_user(self, sns_api_account: SnsApiAccount) -> SnsUserAccountDto:
        pass

    def fetch_posts(self, sns_api_account: SnsApiAccount) -> list[PostDto]:
        pass

    def create_fetch_user_url(self, sns_api_account: SnsApiAccount) -> str:
        pass

    def create_fetch_posts_url(self, sns_api_account: SnsApiAccount) -> str:
        pass

    def convert_user_dto(self, response: Response) -> SnsUserAccountDto:
        pass

    def convert_posts_dto(self, response: Response) -> list[PostDto]:
        pass
