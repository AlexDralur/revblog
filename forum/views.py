from django.shortcuts import render
from django.views import generic
from .models import Category


class CategoryList(generic.ListView):
    model = Category
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8
