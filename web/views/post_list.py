from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from web.components.common.template import get_template_name
from web.models import Post


class PostListView(LoginRequiredMixin, generic.ListView):
    template_name = get_template_name("post_list.html")
    model = Post
    context_object_name = "post_list"
