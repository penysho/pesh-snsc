import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from web.components.common.template import get_template_name
from web.handlers.index import IndexHandler

logger = logging.getLogger(__name__)


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = get_template_name("index.html")

    def post(self, request, *args, **kwargs):
        index_handler = IndexHandler(request=request)
        site = index_handler.change_site()
        logger.info(
            f"ユーザー {request.user.id}: {site.name}にセッションを変更しました"
        )
        return render(request, self.template_name, context=self.kwargs)
