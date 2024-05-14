from abc import ABC, abstractmethod

from django.contrib.auth.forms import AuthenticationForm

from web.models import Site


class LoginService(ABC):

    @abstractmethod
    def create_site(self, form: AuthenticationForm) -> Site:
        pass
