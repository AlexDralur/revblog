from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Category, Post, UserLike
from .forms import PostForm


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

    def form_valid(self, form):

        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
