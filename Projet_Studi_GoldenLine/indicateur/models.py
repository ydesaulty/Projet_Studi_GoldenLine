from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    prix_unitaire = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Prix_unitaire")
    categorie_achat = models.IntegerField()

class Csp(models.Model):
    id_csp = models.AutoField(primary_key=True)
    csp_lbl = models.CharField(max_length=25)

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    nb_enfant = models.IntegerField()
    ville = models.CharField(max_length=25)
    id_csp = models.ForeignKey(Csp, related_name='csps', on_delete=models.DO_NOTHING, default='6')
    
class Collecte(models.Model):
    id_collecte = models.AutoField(primary_key=True)
    prix_categorie = models.DecimalField(max_digits=8, decimal_places=2)
    date_collecte = models.DateTimeField(auto_now_add=True)
    montant_achat = models.DecimalField(max_digits=5, decimal_places=2)
    id_client = models.ForeignKey(Client, related_name='collectes', on_delete=models.DO_NOTHING)
    id_article = models.ForeignKey(Article, related_name='collectes', on_delete=models.DO_NOTHING)
    qte_article = models.IntegerField()
    
    def save(self):
         self.montant_achat = self.id_article.prix_unitaire * self.qte_article
         super().save()
 