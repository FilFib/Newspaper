from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User

"""Concrete View Classes"""

class ListCreateArticcles(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        # if self.request.method == 'GET':
        #     permission_classes = [permissions.IsAdminUser]
        # else:
        #     permission_classes = [permissions.AllowAny]
        return [permissions.IsAdminUser() if self.requestmethod == 'GET' 
                else permissions.AllowAny()] #short if