import logging

import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from web.components.common.session import get_current_site_id
from web.components.common.template import get_template_name
from web.components.instagram.request import create_ig_get_user_url
from web.sevices.sns import SnsService
from web.sevices.sns_api_account import SnsApiAccountServise
from web.sevices.sns_user_account import SnsUserAccountServise

logger = logging.getLogger(__name__)


class SiteRegisterView(LoginRequiredMixin, generic.View):
    template_name = get_template_name("site_register.html")

    def get(self, request, *args, **kwargs):
        current_site_id = get_current_site_id(request.session)

        context = {
            "sns": SnsService(current_site_id).fetch_sns_list(),
            "sns_api_account": SnsApiAccountServise(
                current_site_id
            ).fetch_sns_api_accounts(),
            "sns_user_account": SnsUserAccountServise(
                current_site_id
            ).fetch_sns_user_accounts(),
        }
        return render(request, SiteRegisterView.template_name, context)

    def post(self, request, *args, **kwargs):
        current_site_id = get_current_site_id(request.session)

        sns_api_account = SnsApiAccountServise(
            current_site_id
        ).fetch_sns_api_account_by_type(type="IG")

        sns_user_account, created = SnsUserAccountServise(
            current_site_id
        ).update_or_create_by_ig_response(
            sns=sns_api_account.sns,
            response=requests.get(create_ig_get_user_url(sns_api_account)),
        )
        logger.info(
            f"{'SNSユーザーを登録しました' if created else 'SNSユーザーを更新しました'}: {sns_user_account.name}"
        )
        context = {"key": "登録後"}
        return render(request, SiteRegisterView.template_name, context)
