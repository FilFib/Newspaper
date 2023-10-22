from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

#class based view

class ListCreateArticcles(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):
    def get(self, request, article_id, format=None):
            article= get_object_or_404(Article, id=article_id)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
    
    def put(self, request, article_id, format=None):
        article= get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, article_id, format=None):
        article= get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            article.delete()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


#function methon view

# @api_view(['GET', 'POST'])
# def list_create_articles(request, format=None):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse({'articles': serializer.data})
#     else:
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# @api_view(['GET','PUT','DELETE'])
# def article_detail(request, article_id, format=None):
#     article= get_object_or_404(Article, id=article_id)
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(instance=article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)        


