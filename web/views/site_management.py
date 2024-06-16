import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from injector import AssistedBuilder, Injector

from core.session.implements.session import SnscSessionImpl
from web.components.common.template import get_template_name
from web.modules.site_management import SiteManagementModule
from web.services.site_management.implements.site_management import (
    SiteManagementServiceImpl,
)

logger = logging.getLogger(__name__)


class SiteManagementView(LoginRequiredMixin, generic.View):
    template_name = get_template_name("site_management.html")

    def get(self, request, *args, **kwargs):
        injector = Injector([SiteManagementModule])
        service_builder = injector.get(AssistedBuilder[SiteManagementServiceImpl])
        service = service_builder.build(
            site_id=SnscSessionImpl(request.session).get_current_site_id()
        )

        context = service.create_context_for_get()
        return render(request, SiteManagementView.template_name, context)

    def post(self, request, *args, **kwargs):
        injector = Injector([SiteManagementModule])
        service_builder = injector.get(AssistedBuilder[SiteManagementServiceImpl])
        service = service_builder.build(
            site_id=SnscSessionImpl(request.session).get_current_site_id()
        )

        sns_api_account = service.fetch_sns_api_account(
            type=request.POST.get("sns-type")
        )

        sns_user_account = service.update_or_create_sns_user_account(sns_api_account)
        logger.info(f"SNSユーザーを登録しました: {sns_user_account.name}")

        posts = service.update_or_create_posts(sns_api_account=sns_api_account)
        logger.info(f"SNS投稿を登録/更新しました: {len(posts)}件")

        context = {"sns_user_account": sns_user_account, "posts": posts}
        return render(request, SiteManagementView.template_name, context)
