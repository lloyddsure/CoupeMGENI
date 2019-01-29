import re
from django import forms
from .models import Equipe


class InscriptionForm(forms.ModelForm):

    estConscientDePayer = forms.BooleanField(label="Vous êtes prêt à payer la somme de 180$ (par chèque) pour inscrire l'équipe")

    class Meta:
        model = Equipe
        exclude = ('aPayer',)
        fields = '__all__'
        widgets = {
            'nomEquipe': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'size':'80'}),
            'categorie': forms.Select(attrs={'class': 'mdl-textfield__input'}),
            'nomContact': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'prenomContact': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'emailContact': forms.EmailInput(attrs={'class': 'mdl-textfield__input'}),
            'telephoneContact': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
        }

    def clean_nomEquipe(self):
        nomEquipe = self.cleaned_data['nomEquipe']
        if not re.match("^[0-9A-z\s\-\.]*$", nomEquipe):
            raise forms.ValidationError("Pas de caractère spéciaux, svp !")

        return nomEquipe  # Ne pas oublier de renvoyer le contenu du champ traité

    def clean_nomContact(self):
        nomContact = self.cleaned_data['nomContact']
        if not re.match("^[A-z\s\-\.]*$", nomContact):
            raise forms.ValidationError("Nom invalide !")

        return nomContact  # Ne pas oublier de renvoyer le contenu du champ traité

    def clean_prenomContact(self):
        prenomContact = self.cleaned_data['prenomContact']
        if not re.match("^[A-z\s\-\.]*$", prenomContact):
            raise forms.ValidationError("Prénom invalide !")

        return prenomContact  # Ne pas oublier de renvoyer le contenu du champ traité

    def clean_emailContact(self):
        emailContact = self.cleaned_data['emailContact']
        if not re.match(r"^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$", emailContact):
            raise forms.ValidationError("Adresse couriel invalide !")

        return emailContact  # Ne pas oublier de renvoyer le contenu du champ traité

    def clean_telephoneContact(self):
        telephoneContact = self.cleaned_data['telephoneContact']
        if not re.match("[0-9]{10}",telephoneContact):
            raise forms.ValidationError("Numéro de téléphone invalide !")

        return telephoneContact  # Ne pas oublier de renvoyer le contenu du champ traité

    def clean_estConscientDePayerestConscientDePayer(self):
        estConscientDePayer = self.cleaned_data['estConscientDePayer']
        if not estConscientDePayer:
            raise forms.ValidationError("Vous ne pouvez vous inscrire sans que vous soyez conscient de payer l'inscription")
        return estConscientDePayer

"""
class InscriptionForm(forms.Form):
    equipe = forms.CharField(max_length=100, label="Nom de l'équipe")
    categorie = forms.CharField(max_length=10, label="Catégorie")
    nom = forms.CharField(max_length=100, label="Nom du contact")
    prenom = forms.CharField(max_length=100, label="Prénom de l'équipe")
    email = forms.EmailField(label="Votre adresse e-mail")
    telephone = forms.CharField(max_length=10, label="Votre téléphone")

    def clean_email(self):
        message = self.cleaned_data['email']
        if not "@" in message:
            raise forms.ValidationError("Il n'y a pas de @")

        return message


class MailMassif(forms.Form):
    sujet = forms.CharField(max_length=100, label="Sujet")
    message = forms.CharField(max_length=3000, label="Message")
"""
