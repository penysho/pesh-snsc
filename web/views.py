import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.shortcuts import render
from django.views import generic

from web import models
from web.components.common.template import get_template_name
from web.components.instagram.request import create_ig_get_user_url

from .forms import LoginFrom


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = get_template_name("index.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = get_template_name("login.html")


class LogoutView(LoginRequiredMixin, BaseLogoutView):
    template_name = get_template_name("login.html")


class PostListView(LoginRequiredMixin, generic.ListView):
    template_name = get_template_name("post_list.html")
    model = models.Post
    context_object_name = "post_list"


class SiteRegisterView(LoginRequiredMixin, generic.View):
    template_name = get_template_name("site_register.html")

    def get(self, request, *args, **kwargs):
        context = {"key": "登録前"}
        return render(request, SiteRegisterView.template_name, context)

    def post(self, request, *args, **kwargs):
        user_response = requests.get(
            create_ig_get_user_url(models.Sns.objects.get(site_id=1))
        ).json()
        print(user_response)
        context = {"key": "登録後"}
        return render(request, SiteRegisterView.template_name, context)
