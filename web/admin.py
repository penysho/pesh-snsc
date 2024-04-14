from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.

SnscUser = get_user_model()

admin.site.register(SnscUser)
