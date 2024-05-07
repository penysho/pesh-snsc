from web.apps import WebConfig
from web.components.common.session import SnscSession
from web.sevices.site import SiteService


def get_template_name(file_name: str) -> str:
    return f"{WebConfig.name}/{file_name}"


def get_snsc_context(request) -> dict:
    if request.user.is_authenticated:
        site_service = SiteService(email=request.user.email)
        snsc_session = SnscSession(request.session)
        return {
            "snsc__site_names": [i.name for i in site_service.fetch_sites()],
            "snsc__current_site_name": site_service.fetch_site_by_id(
                id=snsc_session.get_current_site_id()
            ),
        }
    else:
        return {}
