from abc import ABC, abstractmethod

from requests import Response

from web.dto.api import PostDto, SnsUserAccountDto
from web.models.sns_api_account import SnsApiAccount


class ApiRepository(ABC):

    @abstractmethod
    def fetch_user(self, sns_api_account: SnsApiAccount) -> SnsUserAccountDto:
        pass

    @abstractmethod
    def fetch_posts(self, sns_api_account: SnsApiAccount) -> list[PostDto]:
        pass

    @abstractmethod
    def create_fetch_user_url(self, sns_api_account: SnsApiAccount) -> str:
        pass

    @abstractmethod
    def create_fetch_posts_url(self, sns_api_account: SnsApiAccount) -> str:
        pass

    @abstractmethod
    def convert_user_dto(self, response: Response) -> SnsUserAccountDto:
        pass

    @abstractmethod
    def convert_posts_dto(self, response: Response) -> list[PostDto]:
        pass
