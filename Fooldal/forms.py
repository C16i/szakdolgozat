from django import forms
from .models import Termek

class TermekFrom(forms.ModelForm):
    class Meta:
        model = Termek
        fields = ['Azon','Nev','Kategoria','Kiszereles', 'Ar']