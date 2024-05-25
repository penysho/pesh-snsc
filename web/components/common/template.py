from core.session.implements.session import SnscSessionImpl
from web.apps import WebConfig
from web.repositories.site.implements.site import SiteRepositoryImpl


def get_template_name(file_name: str) -> str:
    return f"{WebConfig.name}/{file_name}"


def get_snsc_context(request) -> dict:
    if request.user.is_authenticated:
        site_service = SiteRepositoryImpl()
        snsc_session = SnscSessionImpl(request.session)
        return {
            "snsc__site_names": [
                i.name for i in site_service.fetch_sites(email=request.user.email)
            ],
            "snsc__current_site_name": site_service.fetch_site_by_id(
                id=snsc_session.get_current_site_id()
            ),
        }
    else:
        return {}
