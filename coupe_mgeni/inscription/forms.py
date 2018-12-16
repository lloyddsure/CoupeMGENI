from django import forms
from .models import Equipe


class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = '__all__'
        widgets = {
            'nomEquipe': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'categorie': forms.Select(attrs={'class': 'mdl-textfield__input'}),
            'nomContact': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'prenomContact': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'emailContact': forms.EmailInput(attrs={'class': 'mdl-textfield__input'}),
            'telephoneContact': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
        }


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
"""
