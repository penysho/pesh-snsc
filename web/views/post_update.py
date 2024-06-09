from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from web.components.common.template import get_template_name
from web.forms import PostUpdateForm
from web.forms.post_update import PostProductUpdateFormSet
from web.models import Post
from web.repositories.post.implements.post import PostRepositoryImpl
from web.services.post_update.implements.post_update import PostUpdateServiceImpl

# from django.views import generic


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = get_template_name("post_update.html")
    model = Post
    form_class = PostUpdateForm
    post_product_formset_class = PostProductUpdateFormSet
    success_url = reverse_lazy("web:post_list")

    def get_queryset(self):
        return PostUpdateServiceImpl(post_repository=PostRepositoryImpl()).get_queryset(
            post_id=self.kwargs["pk"]
        )

    def get_context_data(self, **kwargs):
        """contextにformsetを追加する"""
        context = super().get_context_data(**kwargs)
        post_ids = [
            {"posts": self.kwargs["pk"]}
            for _ in range(self.post_product_formset_class.extra)
        ]
        context.update(
            {"post_product_formset": self.post_product_formset_class(initial=post_ids)}
        )
        return context

    def form_valid(self, form):
        """form_classのバリデーション成功後にformsetの処理を追加する"""
        formset = self.post_product_formset_class(
            self.request.POST or None,
        )

        is_success = PostUpdateServiceImpl(
            post_repository=PostRepositoryImpl()
        ).save_post_products(form=form, formset=formset)

        if not is_success:
            return super().form_invalid(formset)

        return super().form_valid(form)
