from django.contrib.auth.views import LoginView as BaseLoginView

from web.components.common.template import get_template_name
from web.forms import LoginFrom
from web.models import Site


class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = get_template_name("login.html")

    def form_valid(self, form):
        self.request.session["current_site"] = Site.objects.filter(
            siteownership__snsc_user__email=form.get_user()
        )[0].id
        print(self.request.session["current_site"])
        return super().form_valid(form)
