from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from core.session.implements.session import SnscSessionImpl
from web.components.common.template import get_template_name
from web.repositories.post.implements.post import PostRepositoryImpl
from web.services.post_list.implements.post_list import PostListServiceImpl


class PostListView(LoginRequiredMixin, generic.ListView):
    template_name = get_template_name("post_list.html")
    context_object_name = "post_list"

    def get_queryset(self):
        queryset = PostListServiceImpl(
            post_repository=PostRepositoryImpl()
        ).get_queryset(
            site_id=SnscSessionImpl(self.request.session).get_current_site_id()
        )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset

    def get_ordering(self):
        """Return the field or fields to use for ordering the queryset."""
        return self.ordering
