from django import forms
from .models import Usuario, Endereco
from django.forms import ValidationError
import re

class Cadastro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'genero', 'email', 'cpf', 'senha', 'telefone', 'data_nascimento', 'nivel')

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 4:
            raise ValidationError('O nome tem que ter no mínimo 4 letras')
        else:
            return nome.upper()[0]
        
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if len(cpf) < 11:
            raise ValidationError('Digite um CPF válido')
        else:
            return cpf
        
    def clean_senha(self):
        senha = self.cleaned_data['senha']
        if len(senha) < 8:
            raise ValidationError('Senha precisa ter no mínimo 8 caracteres')
        if not re.search(r'[a-z]', senha):
            raise ValidationError('Tem que conter no minimo uma letra minuscula')
        if not re.search(r'[A-Z]', senha):
            raise ValidationError('Tem que conter no minimo uma letra maiuscula')
        if not re.search(r'[0-9]', senha):
            raise ValidationError('Tem que conter no minimo um número')
        if not re.search(r'[!@#$%^&*(),.:;?{}[\]\\|<>/~_+-]', senha):
            raise ValidationError('Tem que conter no minimo um simbolo')
        return senha 
    
    def clean_email(self):
        email = self.cleaned_data['email']
        emails_validos = (r'@(gmail\.com|outlook\.com|hotmail\.com|yahoo\.com|'
                          r'uol\.com\.br|bol\.com\.br|terra\.com\.br|globomail\.com)$')
        if not re.search(emails_validos, email):
            raise ValidationError('Digite um email válido')
        else:
            return email
class Endereco(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ('uf', 'cidade', 'bairro', 'rua', 'n', 'complemento')