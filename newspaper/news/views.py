from django.shortcuts import render
import .models import Article
import .serializers import ArticleSerializer

def article_list(request):
    articles = Article.objects.all()
