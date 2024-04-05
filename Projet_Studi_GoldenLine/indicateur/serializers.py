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