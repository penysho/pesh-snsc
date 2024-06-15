from abc import ABC, abstractmethod

import requests
from requests import Response, Session

from web.dto.api import PostDto, SnsUserAccountDto
from web.models.sns_api_account import SnsApiAccount


class ApiRepository(ABC):

    def _get_session(self) -> Session:
        session = Session()
        session.mount(
            "https://",
            requests.adapters.HTTPAdapter(
                max_retries=requests.adapters.Retry(
                    connect=2,
                    read=2,
                    backoff_factor=1,
                    status_forcelist=[500, 502, 503, 504],
                ),
            ),
        )
        return session

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
