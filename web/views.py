import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.shortcuts import render
from django.views import generic

from web.components.common.session import get_current_site
from web.components.common.template import get_template_name
from web.components.instagram.request import create_ig_get_user_url
from web.models import Post, Site, Sns, SnsUserAccount

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

    def form_valid(self, form):
        self.request.session["current_site"] = Site.objects.filter(
            siteownership__snsc_user__email=form.get_user()
        )[0].id
        print(self.request.session["current_site"])
        return super().form_valid(form)


class LogoutView(LoginRequiredMixin, BaseLogoutView):
    template_name = get_template_name("login.html")


class PostListView(LoginRequiredMixin, generic.ListView):
    template_name = get_template_name("post_list.html")
    model = Post
    context_object_name = "post_list"


class SiteRegisterView(LoginRequiredMixin, generic.View):
    template_name = get_template_name("site_register.html")

    def get(self, request, *args, **kwargs):
        context = {"key": "登録前"}
        return render(request, SiteRegisterView.template_name, context)

    def post(self, request, *args, **kwargs):
        current_site = get_current_site(request.session)
        user_response = requests.get(
            create_ig_get_user_url(Sns.objects.get(site_id=current_site))
        ).json()
        print(user_response)
        print(SnsUserAccount.objects.filter(sns__site=current_site))
        # obj, created = SnsUserAccount.objects.update_or_create(
        #     first_name="John",
        #     last_name="Lennon",
        #     defaults={"first_name": "Bob"},
        # )
        context = {"key": "登録後"}
        return render(request, SiteRegisterView.template_name, context)
