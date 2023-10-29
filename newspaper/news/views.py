from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework import generics, permissions, filters
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .paginators import ArticlePaginator

"""Concrete View Classes"""

class ListCreateArticles(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlePaginator
    filter_backends = [filters.OrderingFilter]
    ordering = ['-date']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        return [permissions.IsAdminUser() if self.request.method == 'GET' 
                else permissions.AllowAny()] #short if
    

class APIRoot(APIView):
    def get(self, request, format=None):
        links = {
            'users' : reverse('users', request=request, format=format),
            'articles' : reverse('articles', request=request, format=format),
        }
        return Response(links)
