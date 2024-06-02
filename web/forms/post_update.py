from django import forms

from web.models import Post


class PostUpdateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "投稿タイトルを入力してください。",
                "class": "w-full text-lg form__item",
            }
        )
    )

    status = forms.ChoiceField(
        choices=Post.Status,
        widget=forms.Select(attrs={"class": "form__item"}),
    )

    class Meta:
        model = Post
        fields = ("title", "status")
