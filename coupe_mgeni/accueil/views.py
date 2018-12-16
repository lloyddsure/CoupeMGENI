from django.http import HttpResponse
from django.shortcuts import render
from .models import Accueil,Section
"""
    request: mettre la requete envoyee
    path du template : ne pas oublier de rajouter dans le DIR de settings.py
    arguments en dictionnaire
"""
def home(request):

    accueil = Accueil.objects.all()[0]
    sections = Section.objects.all()
    return render(request, 'accueil/accueil.html', {'accueil':accueil, 'sections':sections})

def view_article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse(
        "Vous avez demandé l'article n° {0} !".format(id_article)
    )
