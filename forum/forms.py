from .models import Post, Comment
from django import Django

class PostForm(forms.Model):
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image',)