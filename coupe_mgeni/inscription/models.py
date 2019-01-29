from django.db import models
from django.utils import timezone


class Categorie(models.Model):
    nom = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Categorie"

    def __str__(self):
        return self.nom




class Equipe(models.Model):
    nomEquipe = models.CharField(max_length=100, verbose_name="Nom de l'équipe")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, verbose_name="Catégorie")
    nomContact = models.CharField(max_length=100, verbose_name="Nom du contact")
    prenomContact = models.CharField(max_length=100, verbose_name="Prénom du contact")
    emailContact = models.CharField(max_length=100, verbose_name="Courriel du contact")
    telephoneContact = models.CharField(max_length=10, verbose_name="Téléphone du contact")
    aPayer = models.BooleanField(verbose_name="A payé", default=False)



    class Meta:
        verbose_name = "Equipe"

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.nomEquipe
