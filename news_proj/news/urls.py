from rest_framework import routers
from news.views import NewsViewSet, CategoryViewSet, NewsCategoryAPIView
from django.urls import path

urlpatterns = [
    path("news/category/<int:cat_id>/", NewsCategoryAPIView.as_view())
]

router = routers.SimpleRouter()
router.register('news', NewsViewSet)
router.register('categories', CategoryViewSet)

urlpatterns += router.urls
