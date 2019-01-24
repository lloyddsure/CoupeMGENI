import csv

from django.contrib import admin
from django.core import serializers
from django.http import HttpResponse

from .models import Categorie, Equipe

def exporter_tableau(modeladmin, request, queryset):

    response = HttpResponse(content_type="text/csv")

    response['Content-Disposition'] = 'attachment; filename="equipes.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nom equipe', 'Categorie', 'Contact', 'Email', 'Telephone'])
    for element in queryset:
        writer.writerow([element.nomEquipe, element.categorie, element.nomContact + " " + element.prenomContact, element.emailContact, element.telephoneContact])


    return response
exporter_tableau.short_description = "Exporter en tableau"

def send_email(modeladmin, request, queryset):
    #queryset.update(status='p')
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)

    return response

send_email.short_description = "Envoyer un email"


class EquipeAdmin(admin.ModelAdmin):
    list_display   = ('nomEquipe', 'categorie', 'apercu_contact', 'emailContact','telephoneContact')
    list_filter    = ('categorie',)
    ordering       = ('categorie', )
    search_fields  = ('nomEquipe', 'categorie')
    actions        = [exporter_tableau, send_email]

    def apercu_contact(self, equipe):
        return equipe.nomContact + " " + equipe.prenomContact

    # En-tête de notre colonne
    apercu_contact.short_description = 'Contact'

admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Categorie)
