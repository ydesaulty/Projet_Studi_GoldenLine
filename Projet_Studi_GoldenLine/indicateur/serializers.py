from rest_framework import serializers

from indicateur.models import Collecte
from indicateur.models import Article
from indicateur.models import Csp
from indicateur.models import Client

class CollecteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collecte
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'

class CspSerializer(serializers.ModelSerializer):

    class Meta:
        model = Csp
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'

class CombinedSerializer(serializers.ModelSerializer):
    id_collecte = serializers.PrimaryKeyRelatedField(read_only=True)
    cat_achat = serializers.IntegerField(source='id_article.categorie_achat')
    prix_categorie = serializers.DecimalField(max_digits=8, decimal_places=2)
    date_collecte = serializers.DateTimeField()
    montant_achat = serializers.DecimalField(max_digits=10, decimal_places=2)
    qte_article = serializers.IntegerField()
    csp_lbl = serializers.CharField(source='id_client.id_csp.csp_lbl')
    description = serializers.CharField(source='id_article.description')

    class Meta:
        model = Collecte
        fields = ['id_collecte', 'cat_achat', 'prix_categorie', 'date_collecte', 'montant_achat', 'qte_article', 'csp_lbl', 'description']
