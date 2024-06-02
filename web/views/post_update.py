from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from web.components.common.template import get_template_name
from web.forms import PostUpdateForm
from web.models import Post
from web.repositories.post.implements.post import PostRepositoryImpl
from web.services.post_update.implements.post_update import PostUpdateServiceImpl

# from django.views import generic


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = get_template_name("post_update.html")
    model = Post
    form_class = PostUpdateForm
    success_url = reverse_lazy("web:post_list")

    def get_queryset(self):
        return PostUpdateServiceImpl(post_repository=PostRepositoryImpl()).get_queryset(
            post_id=self.kwargs["pk"]
        )
