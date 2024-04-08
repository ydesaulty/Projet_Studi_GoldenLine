from django.urls import include, path
from rest_framework import routers

from indicateur.views import CollecteViewSet, ArticleViewSet, CspViewSet

router = routers.DefaultRouter()
router.register(r'collectes', CollecteViewSet, basename='collecte')
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'csps', CspViewSet, basename='csp')

urlpatterns = [
    path('', include(router.urls))
]