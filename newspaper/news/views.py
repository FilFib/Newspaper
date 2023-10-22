from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics

"""Concrete View Classes"""

class ListCreateArticcles(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer