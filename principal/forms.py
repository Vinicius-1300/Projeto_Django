from django import forms
from .models import Usuario

class Cadastro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'cpf', 'senha', 'uf', 'telefone', 'data_nascimento')