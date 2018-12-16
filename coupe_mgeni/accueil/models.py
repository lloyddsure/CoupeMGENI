from django.db import models
from django.utils import timezone
# Create your models here.


class Section(models.Model):
    nom = models.CharField(max_length=100)
    position = models.IntegerField(primary_key=True)
    texte = models.TextField()


    class Meta:
        verbose_name = "Section"
        ordering = ['position']

    def __str__(self):
        return self.nom




class Accueil(models.Model):
    titre = models.CharField(max_length=100, verbose_name="Titre")



    class Meta:
        verbose_name = "Accueil"

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.titre
