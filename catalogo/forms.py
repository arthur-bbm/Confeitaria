from django import forms
from .models import Bolo

class BoloForm(forms.ModelForm):
    class Meta:
        model = Bolo
        fields = ['nome', 'sabor', 'descricao', 'preco', 'disponivel', 'foto']
