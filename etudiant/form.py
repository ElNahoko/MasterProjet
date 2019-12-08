from django import forms
from .models import Etudiant


class DateInput(forms.DateInput):
    input_type = 'date'


class EtudiantForm(forms.ModelForm):

    class Meta:

        model = Etudiant
        fields = '__all__'
        exclude = ['date']
        widgets = {
            'nom':   forms.TextInput(attrs={'class': 'form-control'}),
            'tele':   forms.NumberInput(attrs={'class': 'form-control'}),
            'email':   forms.EmailInput(attrs={'class': 'form-control'}),
            'sexe': forms.Select(attrs={'class': 'form-control'}),
            'prenom':   forms.TextInput(attrs={'class': 'form-control'}),
            'date_naissance':   forms.DateInput(attrs={'class': 'form-control'}),
        }
