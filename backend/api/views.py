from django.shortcuts import render
import feedparser
from rest_framework.generics import ListAPIView
from .serializers import FeedSerializer, FavoriteArticleSerializer
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .models import Article
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UserFavoriteArticles
class TwentyResultsPage(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 21


class FeedView(ListAPIView):
    serializer_class = FeedSerializer
    pagination_class = TwentyResultsPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'source', 'description']

    def get_queryset(self):
        return Article.objects.all().order_by('-published')
    
class FavoritesViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserFavoriteArticles.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)