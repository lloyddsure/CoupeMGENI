from django.http import HttpResponse
from django.shortcuts import render
from .forms import InscriptionForm
from .logic import confirmerInscription


# Create your views here.

def home(request):
    return render(request, 'inscription.html', {})


def  inscription(request):

    if request.method == "POST":
        # Construire le formulaire, soit avec les données postées,
        # soit vide si l'utilisateur accède pour la première fois
        # à la page.
        print("Inscription")

        form = InscriptionForm(request.POST)
        # Nous vérifions que les données envoyées sont valides
        # Cette méthode renvoie False s'il n'y a pas de données
        # dans le formulaire ou qu'il contient des erreurs.
        if form.is_valid():
            # Ici nous pouvons traiter les données du formulaire
            envoi = True
            form.save()
            confirmerInscription(form)
            #utils.mail.envoi_de_mail()
        # Quoiqu'il arrive, on affiche la page du formulaire.
        return render(request, 'inscription.html', locals())
    else:
        form = InscriptionForm(initial={})
        return render(request, 'inscription.html', locals())


def envoi_de_mail(request):
    print(request)
