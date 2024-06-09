from django.forms import BaseModelForm, BaseModelFormSet

from web.models import Post
from web.services.post_update.post_update import PostUpdateService


class PostUpdateServiceImpl(PostUpdateService):

    def __init__(self, post_repository) -> None:
        self.post_repository = post_repository

    def get_queryset(self, post_id: int) -> Post:
        return self.post_repository.fetch_post_by_id(id=post_id)

    def save_post_products(
        self, form: BaseModelForm, formset: BaseModelFormSet
    ) -> bool:
        if not formset.is_valid():
            return False

        post = form.save(commit=False)
        products = formset.save()
        for product in products:
            post.post_products.add(product)

        return True
