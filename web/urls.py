from django.urls import path

from . import views

# https://docs.djangoproject.com/ja/5.0/intro/tutorial03/#namespacing-url-names
app_name = "web"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("post-list/", views.PostListView.as_view(), name="post_list"),
]
