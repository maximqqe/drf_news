from rest_framework import viewsets
from news.models import News, Category
from news.serializers import NewsSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
