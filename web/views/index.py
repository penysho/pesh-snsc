import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from web.components.common.session import SnscSession
from web.components.common.template import get_template_name
from web.repositories.site.implements.site import SiteRepositoryImpl
from web.services.index.implements.index import IndexServiceImpl

logger = logging.getLogger(__name__)


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = get_template_name("index.html")

    def post(self, request, *args, **kwargs):
        service = IndexServiceImpl(
            session=SnscSession(request.session), site_repository=SiteRepositoryImpl()
        )
        site = service.change_site(request=request)
        logger.info(
            f"ユーザー {request.user.id}: {site.name}にセッションを変更しました"
        )
        return render(request, self.template_name, context=self.kwargs)
