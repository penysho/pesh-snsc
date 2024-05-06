import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from web.components.common.session import get_current_site_id
from web.components.common.template import get_template_name
from web.handlers.site_register import SiteRegisterHandler
from web.sevices.sns import SnsService
from web.sevices.sns_api_account import SnsApiAccountServise
from web.sevices.sns_user_account import SnsUserAccountServise

logger = logging.getLogger(__name__)


class SiteRegisterView(LoginRequiredMixin, generic.View):
    template_name = get_template_name("site_register.html")

    def get(self, request, *args, **kwargs):
        current_site_id = get_current_site_id(request.session)

        context = {
            "sns_list": SnsService(current_site_id).fetch_sns_list(),
            "sns_api_accounts": SnsApiAccountServise(
                current_site_id
            ).fetch_sns_api_accounts(),
            "sns_user_accounts": SnsUserAccountServise(
                current_site_id
            ).fetch_sns_user_accounts(),
        }
        return render(request, SiteRegisterView.template_name, context)

    def post(self, request, *args, **kwargs):
        current_site_id = get_current_site_id(request.session)

        sns_api_account = SnsApiAccountServise(
            current_site_id
        ).fetch_sns_api_account_by_type(type="IG")

        handler = SiteRegisterHandler(current_site_id)

        sns_user_account, created = handler.update_or_create_sns_user_account(
            sns_api_account
        )
        logger.info(
            f"{'SNSユーザーを登録しました' if created else 'SNSユーザーを更新しました'}: {sns_user_account.name}"
        )

        handler.update_or_create_post(sns_api_account)

        context = {"sns_user_account": sns_user_account}
        return render(request, SiteRegisterView.template_name, context)
