from django.contrib import admin
from .models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on',)
    list_display = ('title', 'slug', 'created_on')
    search_fields = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'category')
    list_display = ('title', 'slug', 'created_on', 'category')
    search_fields = ('title', 'category')


admin.site.register(Comment)
