import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from web.components.common.session import get_current_site
from web.components.common.template import get_template_name
from web.components.instagram.request import create_ig_get_user_url
from web.models import SnsApiAccount
from web.sevices.sns_api_account import SnsApiAccountServise


class SiteRegisterView(LoginRequiredMixin, generic.View):
    template_name = get_template_name("site_register.html")

    def get(self, request, *args, **kwargs):
        context = {"key": "登録前"}
        current_site = get_current_site(request.session)
        o = SnsApiAccount.objects.select_related("sns").get(
            sns__site_id=current_site, sns__type="IG", sns__is_active=True
        )
        print(o.api_account_id)
        print(o.sns.username)
        return render(request, SiteRegisterView.template_name, context)

    def post(self, request, *args, **kwargs):
        current_site = get_current_site(request.session)
        user_response = requests.get(
            create_ig_get_user_url(
                SnsApiAccountServise.fetch_sns_api_account_by_site(current_site)
            )
        ).json()
        print(user_response)
        context = {"key": "登録後"}
        return render(request, SiteRegisterView.template_name, context)
