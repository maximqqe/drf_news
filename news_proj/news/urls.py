from rest_framework import routers
from news.views import NewsViewSet, CategoryViewSet

urlpatterns = [

]

router = routers.SimpleRouter()
router.register('news', NewsViewSet)
router.register('categories', CategoryViewSet)

urlpatterns += router.urls
