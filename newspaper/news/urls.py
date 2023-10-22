from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.list_create_articles, name='articles'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
]