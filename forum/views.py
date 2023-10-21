from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Category, Post, UserLike
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.utils.text import slugify


class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class CategoryDetail(View):
    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=slug)
        posts = Post.objects.filter(category=category).order_by('-created_on')

        liked_posts = []
        if request.user.is_authenticated:
            liked_posts = UserLike.objects.filter(
                user=request.user, post__in=posts).values_list('post_id', flat=True)

        return render(
            request,
            'posts_list.html',
            {
                'category': category,
                'posts': posts,
                'liked_posts': liked_posts,
            },
        )


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_new.html'

    def get_initial(self):
        category_slug = self.kwargs.get('category_slug')
        category = get_object_or_404(Category, slug=category_slug)
        return {'category': category}

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        form.instance.category = form.cleaned_data['category']
        return super().form_valid(form)
