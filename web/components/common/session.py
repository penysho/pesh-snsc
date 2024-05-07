from django.contrib.sessions.backends.base import SessionBase
from django.core import serializers
from django.forms.models import model_to_dict

from web.models import Site


class SnscSession:

    def __init__(self, session: SessionBase):
        self.session = session

    def get_current_site_id(self) -> str:
        return "1"

    def create_current_site(self, site: Site) -> str:
        # https://stackoverflow.com/questions/21925671/convert-django-model-object-to-dict-with-all-of-the-fields-intact
        site = model_to_dict(site)
        site.pop("snsc_users")
        self.session["current_site"] = site
        return self.session["current_site"]

    def create_sites(self, sites: list[Site]) -> str:
        self.session["sites"] = serializers.serialize("json", sites)
        return self.session["sites"]
