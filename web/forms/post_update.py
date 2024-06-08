from django import forms

from web.models import Post


class PostUpdateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "タイトルを入力してください",
                "class": "w-full text-xl form__item",
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
