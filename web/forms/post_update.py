from enum import Enum

from django import forms

from web.models import Post, PostProduct


class PostProductUpdateFormSetting(Enum):
    MAX_NUM = 10
    EXTRA = 3
    VALIDATE_MAX = True
    CAN_ORDER = True
    CAN_DELETE = True
    CAN_DELETE_EXTRA = False


class PostUpdateForm(forms.ModelForm):
    title = forms.CharField(
        label="投稿タイトル",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "タイトルを入力してください",
                "class": "form__item w-full bg-gray-100 rounded-lg p-1",
            }
        ),
    )
    status = forms.ChoiceField(
        label="投稿ステータス",
        choices=Post.Status,
        widget=forms.Select(attrs={"class": "form__item bg-gray-100"}),
    )

    class Meta:
        model = Post
        fields = ("title", "status")


class PostProductUpdateForm(forms.ModelForm):
    name = forms.CharField(
        label="投稿に紐づく商品名",
        widget=forms.TextInput(
            attrs={
                "placeholder": "商品名を入力してください。",
                "class": "form__item basis-3/5 bg-gray-300 rounded-lg p-1",
            }
        ),
    )
    page_url = forms.URLField(
        label="商品ページURL",
        widget=forms.TextInput(
            attrs={
                "placeholder": "https://example.com/product/1",
                "class": "form__item basis-3/5 bg-gray-300 rounded-lg p-1",
            },
        ),
    )
    image_url = forms.URLField(
        label="商品画像URL",
        widget=forms.TextInput(
            attrs={
                "placeholder": "https://example.com/product/image.jpg",
                "class": "form__item shrink basis-3/5 bg-gray-300 rounded-lg p-1",
            }
        ),
    )

    class Meta:
        model = PostProduct
        # idについて登録時は自動で付与されるが、更新時に指定が必要
        # postsは指定せずともsave()で保存されるため指定不要
        fields = ("id", "name", "page_url", "image_url")


class BasePostProductUpdateFormSet(forms.BaseModelFormSet):
    deletion_widget = forms.CheckboxInput(
        attrs={
            "class": "form__item",
        }
    )


PostProductUpdateFormSet = forms.modelformset_factory(
    model=PostProduct,
    form=PostProductUpdateForm,
    formset=BasePostProductUpdateFormSet,
    max_num=PostProductUpdateFormSetting.MAX_NUM.value,
    extra=PostProductUpdateFormSetting.EXTRA.value,
    validate_max=PostProductUpdateFormSetting.VALIDATE_MAX.value,
    can_order=PostProductUpdateFormSetting.CAN_ORDER.value,
    can_delete=PostProductUpdateFormSetting.CAN_DELETE.value,
    can_delete_extra=PostProductUpdateFormSetting.CAN_DELETE_EXTRA.value,
)
