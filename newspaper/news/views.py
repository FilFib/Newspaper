from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User

"""Concrete View Classes"""

class ListCreateArticcles(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer