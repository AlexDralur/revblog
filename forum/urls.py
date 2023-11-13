from . import views
from django.urls import path, include
from .views import PostCreateView, PostUpdateView, PostDeleteView, FavouritePost, LikedPost, CommentUpdateView

urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('<slug:slug>/', views.CategoryDetail.as_view(), name='posts_list'),
    path('accounts/', include('allauth.urls')),
    path('<slug:category_slug>/create/',
         PostCreateView.as_view(), name='create_post'),
    path('<slug:category_slug>/<slug:post_slug>/',
         views.PostDetail.as_view(), name='post_detail'),
    path('<slug:category_slug>/<slug:post_slug>/edit/',
         PostUpdateView.as_view(), name='update_post'),
    path('<slug:category_slug>/<slug:post_slug>/delete/',
         views.PostDeleteView.as_view(), name='delete_post'),
    path('<slug:category_slug>/<slug:post_slug>/favourite/',
         views.FavouritePost.as_view(), name='favourite'),
    path('<slug:category_slug>/<slug:post_slug>/like/',
         views.LikedPost.as_view(), name='like'),
    path('<slug:category_slug>/<slug:post_slug>/update_comment/',
         views.CommentUpdateView.as_view(), name='update_comment')
]
