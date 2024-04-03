from django.contrib import admin

from indicateur.models import Article, Csp, Collecte

@admin.register(Csp)
class CspAdmin(admin.ModelAdmin):
    list_display = ('id_csp', 'csp_lbl')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('categorie_achat', 'description', 'prix_unitaire')

@admin.register(Collecte)
class CollecteAdmin(admin.ModelAdmin):
    list_display = ('id_collecte', 'date_collecte', 'prix_categorie', 'qte_article', 'montant_achat')

