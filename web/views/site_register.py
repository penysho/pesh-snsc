import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from web.components.common.session import SnscSession
from web.components.common.template import get_template_name
from web.services.site_register.implements.site_register import SiteRegisterServiceImpl

logger = logging.getLogger(__name__)


class SiteRegisterView(LoginRequiredMixin, generic.View):
    template_name = get_template_name("site_register.html")

    def get(self, request, *args, **kwargs):
        session = SnscSession(request.session)
        current_site_id = session.get_current_site_id()
        service = SiteRegisterServiceImpl(current_site_id)
        context = service.create_context_for_get()
        return render(request, SiteRegisterView.template_name, context)

    def post(self, request, *args, **kwargs):
        session = SnscSession(request.session)
        current_site_id = session.get_current_site_id()
        service = SiteRegisterServiceImpl(current_site_id)

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
        return render(request, SiteRegisterView.template_name, context)
