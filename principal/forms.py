from django import forms
from .models import Usuario, Endereco

class Cadastro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'genero', 'email', 'cpf', 'senha', 'telefone', 'data_nascimento')

class Endereco(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ('uf', 'cidade', 'bairro', 'rua', 'n', 'complemento')