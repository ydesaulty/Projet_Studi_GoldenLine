from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter

from indicateur.models import Collecte, Article, Csp, Client

from indicateur.serializers import CollecteSerializer, ArticleSerializer, CspSerializer, CombinedSerializer

class CollecteViewSet(viewsets.ModelViewSet):
    
    serializer_class = CollecteSerializer

    def get_queryset(self):
        queryset = Collecte.objects.filter()
        id_client = self.request.GET.get('id_client')
        if id_client :
            queryset = queryset.filter(id_client=id_client)
        return queryset
         

class ArticleViewSet(viewsets.ModelViewSet):
    
    serializer_class = ArticleSerializer
    
    queryset = Article.objects.all()    
    filterset_fields = ['categorie_achat', 'description']
    search_fields = ['description']

class CspViewSet(viewsets.ModelViewSet):

    serializer_class = CspSerializer
    
    def get_queryset(self):        
        return Csp.objects.filter()

class CombinedModelViewSet(viewsets.ModelViewSet):
    
    serializer_class = CombinedSerializer

    def get_queryset(self):
        return Collecte.objects.all()
    
    queryset = Collecte.objects.all()

