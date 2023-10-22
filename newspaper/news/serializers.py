from .models import Article
from django.contrib.auth.models import User
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'owner', 'date')


class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(
        queryset=Article.objects.all(), many=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'articles')

