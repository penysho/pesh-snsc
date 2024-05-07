import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from web.components.common.template import get_template_name
from web.handlers.index import IndexHandler

logger = logging.getLogger(__name__)


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = get_template_name("index.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        handler = IndexHandler()
        site = handler.change_site(request)
        logger.info(
            f"{site.name}にセッションを変更しました: ユーザーID: {request.user.id}"
        )
        return render(request, self.template_name, context=self.kwargs)
