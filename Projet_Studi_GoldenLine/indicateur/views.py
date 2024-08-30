from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from indicateur.models import Collecte, Article, Csp, Client

from indicateur.serializers import CollecteSerializer, ArticleSerializer, CspSerializer, CombinedSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class HomeView(APIView):
     
   permission_classes = (IsAuthenticated, )
   def get(self, request):
        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
        return Response(content)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response({"error": "Le refresh_token est manquant."}, status=status.HTTP_400_BAD_REQUEST)            
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

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
        'date_collecte': ['gte', 'lte']
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        csp = self.request.query_params.get('csp')
        category = self.request.query_params.get('cat_achat')
        start_date = self.request.query_params.get('start_date')  
        end_date = self.request.query_params.get('end_date')  

        print(f"csp: {csp}, cat_achat: {category}, start_date: {start_date}, end_date: {end_date}")  # Impression de débogage

        if csp:
            queryset = queryset.filter(id_client__id_csp__csp_lbl=csp)
        if category:
            queryset = queryset.filter(id_article__categorie_achat=category)
        if start_date:
            queryset = queryset.filter(date_collecte__gte=start_date)
        if end_date:
            queryset = queryset.filter(date_collecte__lte=end_date)
        
        print(f"Queryset: {queryset.query}")  # Impression de débogage

        return queryset
