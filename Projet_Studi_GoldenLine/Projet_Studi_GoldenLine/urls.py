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
      title="API GoldenLine",
      default_version='v1',
      description="API RESTful développée à partir des frameworks Django et Django REST Framework (DRF). "
                  "Cette API est conçue pour gérer et exposer des ressources relatives au projet GoldenLine. "
                  "Elle a pour objectif de renvoyer les données relatives aux collectes de manière anonymisée, "
                  "et selon les critères définis via le frontend et au format JSON. \n\n"
                  "L'API prend en charge l'authentification via JSON Web Tokens (JWT), garantissant une communication "
                  "sécurisée et l'accès autorisé aux ressources. Les utilisateurs doivent s'authentifier pour pouvoir "
                  "accéder aux données, tandis que des fonctionnalités de filtrage et de recherche sont disponibles "
                  "pour faciliter l'accès aux données demandées.\n\n"
                  "Les principales fonctionnalités de l'API incluent :\n"
                  " • Gestion des utilisateurs : via l’interface d’administration, Création, mise à jour, et gestion des profils utilisateurs.\n"
                  " • Authentification sécurisée : Utilisation de JWT pour sécuriser l'accès aux endpoints.\n"
                  " • Gestion des indicateurs : Création, mise à jour, suppression, et récupération des indicateurs de performance.\n"
                  " • Filtrage et recherche : via l’interface d’administration, Recherche avancée et filtrage dynamique des données grâce à l'intégration de Django Filters.\n"
                  " • Support CORS : Support des requêtes Cross-Origin pour une intégration front-end fluide.\n\n"
                  "Cette API est destinée à être utilisée avec l’application front-end.",
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
