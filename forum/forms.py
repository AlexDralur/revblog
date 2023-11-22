from .models import Post, Comment
from django import forms


class PostForm(forms.ModelForm):
    """ FORM TO HANDLE POSTS """

    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image', 'category',)


class CommentForm(forms.ModelForm):
    """ FORM TO HANDLE COMMENTS """

    class Meta:
        model = Comment
        fields = ('body',)
