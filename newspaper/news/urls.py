from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('articles/', views.ListCreateArticcles.as_view(), name='articles'),
    path('articles/<int:article_id>/', views.ArticleDetails.as_view(), name='article_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)