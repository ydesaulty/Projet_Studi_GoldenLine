from rest_framework import routers

from indicateur.views import CollecteViewSet, ArticleViewSet, CspViewSet

router = routers.DefaultRouter()
router.register('collectes', CollecteViewSet)
router.register('articles', ArticleViewSet)
router.register('csps', CspViewSet)