from django.contrib.sessions.backends.base import SessionBase


def get_current_site(session: SessionBase):
    return session["current_site"]
