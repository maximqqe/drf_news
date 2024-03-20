from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
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

    @method_decorator(cache_page(10, key_prefix="news-list"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60*5, key_prefix="news"))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @method_decorator(cache_page(10, key_prefix="category-list"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60*5, key_prefix="category"))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class NewsCategoryAPIView(ListAPIView):
    serializer_class = NewsSerializer
    lookup_url_kwarg = 'cat_id'
    pagination_class = NewsPagination

    def get_queryset(self):
        cat_id = self.kwargs.get(self.lookup_url_kwarg)
        queryset = News.objects.filter(category=cat_id)
        return queryset

    @method_decorator(cache_page(timeout=10, key_prefix='news-category'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
