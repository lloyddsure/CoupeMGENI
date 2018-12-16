from django.contrib import admin

# Register your models here.
from .models import Accueil,Section

class AccueilAdmin(admin.ModelAdmin):
    list_display   = ('titre',)
    list_filter    = ()
    search_fields  = ('titre',)

class SectionAdmin(admin.ModelAdmin):
    list_display   = ('nom', 'position', 'texte')
    list_filter    = ()
    search_fields  = ('titre', 'texte')


admin.site.register(Accueil, AccueilAdmin)
admin.site.register(Section, SectionAdmin)
