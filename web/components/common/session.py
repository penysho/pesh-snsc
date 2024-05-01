from django.contrib.sessions.backends.base import SessionBase


def get_current_site_id(session: SessionBase):
    return session["current_site_id"]
