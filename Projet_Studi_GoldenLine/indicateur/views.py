from django.shortcuts import render
from rest_framework import viewsets

from indicateur.models import Collecte, Article, Csp

from indicateur.serializers import CollecteSerializer, ArticleSerializer, CspSerializer

class CollecteViewSet(viewsets.ModelViewSet):
    
    queryset = Collecte.objects.all()
    serializer_class = CollecteSerializer
    filterset_fields = ['date_collecte', 'montant_achat']

class ArticleViewSet(viewsets.ModelViewSet):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['categorie_achat', 'description']
    search_fields = ['description']

class CspViewSet(viewsets.ModelViewSet):
    
    queryset = Csp.objects.all()
    serializer_class = CspSerializer
    filterset_fields = ['id_csp', 'csp_lbl']
    search_fields = ['csp_lbl']

