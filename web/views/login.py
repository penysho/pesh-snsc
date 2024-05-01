from django.contrib.auth.views import LoginView as BaseLoginView

from web.components.common.template import get_template_name
from web.forms import LoginFrom
from web.sevices.site import SiteService


class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = get_template_name("login.html")

    def form_valid(self, form):
        site_service = SiteService()
        self.request.session["current_site_id"] = site_service.fetch_sites(
            email=form.get_user()
        )[0].id
        return super().form_valid(form)
