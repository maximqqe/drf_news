from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from news.models import News, Category
from news.serializers import NewsSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class NewsPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 50


class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
