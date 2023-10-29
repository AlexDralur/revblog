from . import views
from django.urls import path, include
from .views import PostCreateView, PostUpdateView

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
]
