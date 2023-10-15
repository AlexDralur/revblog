from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('<slug:slug>/', views.CategoryDetail.as_view(), name='posts_list'),
    path('accounts/', include('allauth.urls')),
]
