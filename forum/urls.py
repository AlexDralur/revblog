from . import views
from django.urls import path, include
from .views import PostCreateView

urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('<slug:slug>/', views.CategoryDetail.as_view(), name='posts_list'),
    path('accounts/', include('allauth.urls')),
    path('create/', PostCreateView.as_view(), name='create_post')
]
