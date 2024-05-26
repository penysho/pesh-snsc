from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from core.session.implements.session import SnscSessionImpl
from web.components.common.template import get_template_name
from web.forms import PostUpdateForm
from web.models import Post
from web.repositories.post.implements.post import PostRepositoryImpl
from web.services.post_list.implements.post_list import PostListServiceImpl


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = get_template_name("post_update.html")
    model = Post
    form_class = PostUpdateForm

    def get_queryset(self):
        return PostListServiceImpl(post_repository=PostRepositoryImpl()).get_queryset(
            site_id=SnscSessionImpl(self.request.session).get_current_site_id()
        )
