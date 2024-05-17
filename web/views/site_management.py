import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from injector import AssistedBuilder, Injector

from web.components.common.session import SnscSession
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
            site_id=SnscSession(request.session).get_current_site_id()
        )

        context = service.create_context_for_get()
        return render(request, SiteManagementView.template_name, context)

    def post(self, request, *args, **kwargs):
        injector = Injector([SiteManagementModule])
        service_builder = injector.get(AssistedBuilder[SiteManagementServiceImpl])
        service = service_builder.build(
            site_id=SnscSession(request.session).get_current_site_id()
        )

        # session = SnscSession(request.session)
        # current_site_id = session.get_current_site_id()
        # service = SiteManagementServiceImpl(current_site_id, InstagramRepositoryImpl())

        sns_api_account = service.fetch_sns_api_account(type="IG")

        sns_user_account, created = service.update_or_create_sns_user_account(
            sns_api_account
        )
        logger.info(
            f"{'SNSユーザーを登録しました' if created else 'SNSユーザーを更新しました'}: {sns_user_account.name}"
        )

        posts = service.update_or_create_post(sns_api_account)
        logger.info(f"SNS投稿を登録/更新しました: {len(posts)}件")

        context = {"sns_user_account": sns_user_account, "posts": posts}
        return render(request, SiteManagementView.template_name, context)