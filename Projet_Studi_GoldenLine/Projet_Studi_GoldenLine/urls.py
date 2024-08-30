"""
URL configuration for Projet_Studi_GoldenLine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views
from .views import index
from django.urls import include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions
from indicateur.urls import router as indicateur_routeur
from rest_framework_simplejwt import views as jwt_views
from indicateur.views import HomeView, LogoutView

schema_view = get_schema_view(
   openapi.Info(
      title="Collecte API",
      default_version='v1',
      description="API utilisee pour generer un indicateur de panier moyen",
      contact=openapi.Contact(email="yrae9@hotmail.com"),      
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.registry.extend(indicateur_routeur.registry)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include(router.urls)),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
   path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
   path('home/', HomeView.as_view(), name ='home'),
   path('logout/', LogoutView.as_view(), name ='logout')
]
