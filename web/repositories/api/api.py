from abc import ABC, abstractmethod

from requests import Response

from web.dto.api import PostDto
from web.models.sns_api_account import SnsApiAccount


class ApiRepository(ABC):

    @abstractmethod
    def fetch_user(self, sns_api_account: SnsApiAccount) -> dict:
        pass

    @abstractmethod
    def fetch_post(self, sns_api_account: SnsApiAccount) -> list[PostDto]:
        pass

    @abstractmethod
    def create_fetch_user_url(self, sns_api_account: SnsApiAccount) -> str:
        pass

    @abstractmethod
    def create_fetch_post_url(self, sns_api_account: SnsApiAccount) -> str:
        pass

    @abstractmethod
    def convert_user_dto(self, response: Response) -> dict:
        pass

    @abstractmethod
    def convert_post_dto(self, response: Response) -> list[PostDto]:
        pass
