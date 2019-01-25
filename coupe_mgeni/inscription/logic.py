import utils.mail


def confirmerInscription(formEquipe):
    equipe = formEquipe.cleaned_data['nomEquipe']
    categorie = formEquipe.cleaned_data['categorie']

    subject = "Inscription Coupe MGENI"
    message = """Bonjour, \n vous etes inscrits pour le tournoi avec l'equipe {nom_equipe} dans la categorie {categorie}""".format(nom_equipe=equipe, categorie=categorie)
    sender = "info@coupemgeni.com"
    to = formEquipe.cleaned_data['emailContact']
    utils.mail.envoi_de_mail(subject,message,sender,to)
