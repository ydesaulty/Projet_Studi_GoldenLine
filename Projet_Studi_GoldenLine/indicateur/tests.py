from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Article, Csp, Collecte, Client
from .serializers import CollecteSerializer, CombinedSerializer
from decimal import Decimal
from datetime import datetime, timedelta

class ModelTests(TestCase):
    def setUp(self):
        self.csp = Csp.objects.create(csp_lbl="Employes")
        self.client = Client.objects.create(
            nom="Doe", 
            prenom="John", 
            mail="john@example.com", 
            nb_enfant=2, 
            ville="Paris", 
            id_csp=self.csp
        )
        self.article = Article.objects.create(
            description="Test Article",
            prix_unitaire=10.00,
            categorie_achat=1
        )

    def test_csp_creation(self):
        self.assertEqual(self.csp.csp_lbl, "Employes")

    def test_client_creation(self):
        self.assertEqual(self.client.nom, "Doe")
        self.assertEqual(self.client.id_csp, self.csp)

    def test_article_creation(self):
        self.assertEqual(self.article.description, "Test Article")
        self.assertEqual(self.article.prix_unitaire, Decimal('10.00'))

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)
        
        self.csp = Csp.objects.create(csp_lbl="Employes")
        self.client_obj = Client.objects.create(
            nom="Doe", 
            prenom="John", 
            mail="john@example.com", 
            nb_enfant=2, 
            ville="Paris", 
            id_csp=self.csp
        )
        self.article = Article.objects.create(
            description="Test Article",
            prix_unitaire=10.00,
            categorie_achat=1
        )
        self.collecte = Collecte.objects.create(
            prix_categorie=10.00,
            montant_achat=20.00,
            id_client=self.client_obj,
            id_article=self.article,
            qte_article=2,
            date_collecte=datetime.now()
        )

    def test_get_combined_view(self):
        response = self.client.get(reverse('combinedviewSet-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)
        
        # Vérifier la structure des données
        first_item = response.data[0]
        expected_fields = ['id_collecte', 'cat_achat', 'prix_categorie', 'date_collecte', 
                           'montant_achat', 'qte_article', 'csp_lbl', 'description']
        for field in expected_fields:
            self.assertIn(field, first_item)

    def test_filter_combined_view_by_csp(self):
        response = self.client.get(reverse('combinedviewSet-list'), {'csp': 'Employes'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for item in response.data:
            self.assertEqual(item['csp_lbl'], 'Employes')

    def test_filter_combined_view_by_category(self):
        response = self.client.get(reverse('combinedviewSet-list'), {'cat_achat': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for item in response.data:
            self.assertEqual(item['cat_achat'], 1)

    def test_filter_combined_view_by_date(self):
        start_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        end_date = datetime.now().strftime('%Y-%m-%d')
        response = self.client.get(reverse('combinedviewSet-list'), 
                                   {'start_date': start_date, 'end_date': end_date})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for item in response.data:
            item_date = datetime.strptime(item['date_collecte'], "%Y-%m-%dT%H:%M:%SZ")
            self.assertTrue(start_date <= item_date.strftime('%Y-%m-%d') <= end_date)

    def test_create_collecte(self):
        data = {
            "prix_categorie": 15.00,
            "montant_achat": 30.00,
            "id_client": self.client_obj.id_client,
            "id_article": self.article.id_article,
            "qte_article": 2
        }
        response = self.client.post(reverse('collecte-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class AuthenticationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.token_url = reverse('token_obtain_pair')

    def test_obtain_token(self):
        response = self.client.post(self.token_url, {'username': 'testuser', 'password': '12345'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)

    def test_access_protected_view(self):
        # Tentative d'accès sans token
        response = self.client.get(reverse('combinedviewSet-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Obtention du token
        token_response = self.client.post(self.token_url, {'username': 'testuser', 'password': '12345'}, format='json')
        token = token_response.data['access']

        # Accès avec token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(reverse('combinedviewSet-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)