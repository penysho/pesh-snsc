from django.contrib.sessions.backends.base import SessionBase

from core.session.session import SnscSession
from web.models import Site


class SnscSessionImpl(SnscSession):

    def __init__(self, session: SessionBase):
        self.session = session

    def get_current_site_id(self) -> int:
        return self.session["current_site_id"]

    def create_current_site(self, site: Site) -> int:
        self.session["current_site_id"] = site.id
        return self.session["current_site_id"]
