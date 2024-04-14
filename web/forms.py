from django.contrib.auth.forms import AuthenticationForm

from web.admin import SnscUser


class LoginFrom(AuthenticationForm):
    class Meta:
        model = SnscUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["placeholder"] = field.label
