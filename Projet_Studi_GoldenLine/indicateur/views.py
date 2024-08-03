from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter

from indicateur.models import Collecte, Article, Csp, Client

from indicateur.serializers import CollecteSerializer, ArticleSerializer, CspSerializer, CombinedSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class CollecteViewSet(viewsets.ModelViewSet):
    serializer_class = CollecteSerializer

    def get_queryset(self):
        queryset = Collecte.objects.all()
        id_client = self.request.GET.get('id_client')
        if id_client:
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
        return Csp.objects.all()

class CombinedModelViewSet(viewsets.ModelViewSet):
    serializer_class = CombinedSerializer
    queryset = Collecte.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        'id_client__id_csp__csp_lbl': ['exact'],
        'id_article__categorie_achat': ['exact'],
        'date_collecte': ['icontains']
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        csp = self.request.query_params.get('csp')
        category = self.request.query_params.get('cat_achat')
        period = self.request.query_params.get('period')

        print(f"csp: {csp}, cat_achat: {category}, period: {period}")  # Impression de débogage

        if csp:
            queryset = queryset.filter(id_client__id_csp__csp_lbl=csp)
        if category:
            queryset = queryset.filter(id_article__categorie_achat=category)
        if period:
            queryset = queryset.filter(date_collecte__icontains=period)

        print(f"Queryset: {queryset.query}")  # Impression de débogage

        return queryset
