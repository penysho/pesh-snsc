import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from web.components.common.template import get_template_name
from web.forms import PostUpdateForm
from web.forms.post_update import PostProductUpdateFormSet
from web.models import Post
from web.repositories.post.implements.post import PostRepositoryImpl
from web.services.post_update.implements.post_update import PostUpdateServiceImpl

logger = logging.getLogger(__name__)


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
            logger.error(f"投稿への商品紐付けに失敗しました: {formset}")
            logger.error(f"Formに関連したエラー: {formset.errors}")
            logger.error(f"Formに関連しないエラー: {formset.non_form_errors()}")
            return super().form_invalid(formset)

        logger.info(f"投稿への商品紐付けに成功しました: {formset}")
        return super().form_valid(form)
