from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Category, Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils.text import slugify
from django.http import HttpResponseRedirect, JsonResponse
from django.utils import timezone
from django.db import IntegrityError


class CategoryList(generic.ListView):
    """ VIEW TO DISPLAY THE LIST OF CATEGORIES """

    model = Category
    queryset = Category.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class CategoryDetail(View):
    """ VIEW TO DISPLAY THE LIST OF POSTS INSIDE A CATEGORY """

    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=slug)
        posts = Post.objects.filter(
            category=category).order_by('-created_on')

        return render(
            request,
            'posts_list.html',
            {
                'category': category,
                'posts': posts,
            },
        )


class PostDetail(DetailView):
    """ VIEW TO DISPLAY A SPECIFIC POST """

    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        category_slug = self.kwargs.get('category_slug')
        post_slug = self.kwargs.get('post_slug')
        return get_object_or_404(
            Post, category__slug=category_slug, slug=post_slug)

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user.username
            new_comment.save()
            messages.success(request, 'Comment was added to post.')
        else:
            messages.error(request, 'Sorry an error occured \
            while saving your comment. Please try again.')

        return redirect('post_detail', category_slug=post.category.slug, post_slug=post.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        post = self.get_object()
        user = self.request.user
        context['favourite'] = post.favourite.filter(id=user.id).exists()
        context['liked'] = post.likes.filter(id=user.id).exists()
        context['comments'] = self.get_object().comments.all()
        return context



class PostCreateView(LoginRequiredMixin, CreateView):
    """ VIEW TO DISPLAY THE FORM TO PUBLISH A NEW POST """

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

        try:
            result = super().form_valid(form)
        except IntegrityError:
            messages.error(
                self.request, "A post with the same title already exists.")
            return self.form_invalid(form)
        
        messages.success(self.request, 'Post published.')
        return result

    def get_success_url(self):
        category_slug = self.kwargs.get('category_slug')
        success_url = reverse_lazy('posts_list', kwargs={
            'slug': category_slug})
        return success_url


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """ VIEW TO DISPLAY THE FORM TO EDIT A POST """

    model = Post
    form_class = PostForm
    template_name = 'post_update.html'
    slug_url_kwarg = 'post_slug'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        form.instance.updated_at = timezone.now()
        return super().form_valid(form)
    
    def handle_image_upload(self, request, post_instance=None):
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES,
                            instance=post_instance)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request,'Your post was updated.')
                return post
            else:
                messages.error(request, 'An error has occured while \
                uploading your image. Please try again.')
                return post
        return None

    def dispatch(self, request, *args, **kwargs):
        post_instance = self.get_object()
        if request.user.is_authenticated:
            self.handle_image_upload(request, post_instance=post_instance)

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        category_slug = self.kwargs.get('category_slug')
        post_slug = self.kwargs.get('post_slug')
        success_url = reverse_lazy(
            'post_detail', kwargs={
                'category_slug': category_slug, 'post_slug': post_slug})
        return success_url


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """ VIEW TO DELETE A POST """

    model = Post
    template_name = 'post_delete.html'
    slug_url_kwarg = 'post_slug'
    success_url = '/'

    def get_object(self, queryset=None):
        category_slug = self.kwargs.get('category_slug')
        post_slug = self.kwargs.get('post_slug')
        messages.success(self.request, 'Post deleted successfully.')
        return Post.objects.get(category__slug=category_slug, slug=post_slug)


class FavouritePost(LoginRequiredMixin, View):
    """ VIEW IF THE USER FAVOURITE A POST """

    def get(self, request, category_slug, post_slug):
        post = get_object_or_404(
            Post, category__slug=category_slug, slug=post_slug)
        favorited = post.favourite.filter(id=request.user.id).exists()

        if favorited:
            post.favourite.remove(request.user)
        else:
            post.favourite.add(request.user)
        return HttpResponseRedirect(
            request.META.get('HTTP_REFERER', reverse_lazy('post')))


class LikedPost(LoginRequiredMixin, View):
    """ VIEW IF THE USER LIKE A POST """

    def get(self, request, category_slug, post_slug):
        post = get_object_or_404(
            Post, category__slug=category_slug, slug=post_slug)
        liked = post.likes.filter(id=request.user.id).exists()

        if liked:
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(
            request.META.get('HTTP_REFERER', reverse_lazy('post')))


class CommentUpdateView(LoginRequiredMixin, View):
    """ VIEW IF THE USER WANTS TO UPDATE A COMMENT """

    template_name = 'update_comment.html'

    def get(self, request, category_slug, post_slug, pk):
        comment_update = get_object_or_404(
            Comment, pk=pk, name=request.user.username)
        form = CommentForm(instance=comment_update)
        context = {'form': form, 'comment': comment_update}
        return render(request, self.template_name, context)

    def post(self, request, category_slug, post_slug, pk):
        comment_update = get_object_or_404(
            Comment, pk=pk, name=request.user.username)
        form = CommentForm(request.POST, instance=comment_update)

        if form.is_valid():
            form.instance.updated_at = timezone.now()
            form.save()
            post_url = reverse_lazy(
                'post_detail', kwargs={
                    'category_slug': category_slug, 'post_slug': post_slug})
            messages.success(request, 'Comment added to post.')
            return redirect(post_url)
        else:
            messages.error(request, 'An error occured. Please try again.')
            return rediract(post_url)

        context = {'form': form, 'comment': comment_update}
        return render(request, self.template_name, context)


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    """ VIEW IF THE USER WANTS TO DELETE A COMMENT """

    model = Comment
    template_name = 'delete_comment.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(
            Comment, pk=pk, name=self.request.user.username)

    def get_success_url(self):
        category_slug = self.kwargs.get('category_slug')
        post_slug = self.kwargs.get('post_slug')
        success_url = reverse_lazy(
            'post_detail', kwargs={
                'category_slug': category_slug, 'post_slug': post_slug})
        messages.success(self.request, 'Comment deleted successfully.')
        return success_url
