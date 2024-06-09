from abc import ABC, abstractmethod

from django.forms import BaseModelForm, BaseModelFormSet

from web.models import Post


class PostUpdateService(ABC):

    @abstractmethod
    def get_queryset(self, post_id: int) -> Post:
        pass

    @abstractmethod
    def save_post_products(
        self, form: BaseModelForm, formset: BaseModelFormSet
    ) -> bool:
        pass
