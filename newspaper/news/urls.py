from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('articles/', views.ListCreateArticcles.as_view(), name='articles'),
    path('articles/<int:pk>/', views.ArticleDetails.as_view(), name='article_detail'),
    path('users/', views.ListUsers.as_view(), name = 'users'),
]

urlpatterns = format_suffix_patterns(urlpatterns)