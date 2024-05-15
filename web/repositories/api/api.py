from abc import ABC, abstractmethod

from requests import Response

from web.models.sns_api_account import SnsApiAccount


class ApiRepository(ABC):

    @abstractmethod
    def fecth_user(self, sns_api_account: SnsApiAccount) -> dict:
        pass

    @abstractmethod
    def fecth_media(self, sns_api_account: SnsApiAccount) -> dict:
        pass

    @abstractmethod
    def create_get_user_url(self, sns_api_account: SnsApiAccount) -> str:
        pass

    @abstractmethod
    def create_get_media_url(self, sns_api_account: SnsApiAccount) -> str:
        pass

    @abstractmethod
    def convert_get_user_for_register(self, response: Response) -> dict:
        pass

    @abstractmethod
    def convert_get_media_for_register(self, response: Response) -> dict:
        pass
