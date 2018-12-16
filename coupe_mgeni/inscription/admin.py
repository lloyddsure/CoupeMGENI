from django.contrib import admin
from .models import Categorie, Equipe

class EquipeAdmin(admin.ModelAdmin):
    list_display   = ('nomEquipe', 'categorie', 'apercu_contact', 'emailContact','telephoneContact')
    list_filter    = ('categorie',)
    ordering       = ('categorie', )
    search_fields  = ('nomEquipe', 'categorie')

    def apercu_contact(self, equipe):
        return equipe.nomContact + " " + equipe.prenomContact

    # En-tête de notre colonne
    apercu_contact.short_description = 'Contact'

admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Categorie)
