from django import forms

from web.models import Post


class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("title",)
