from django.db import models
import random
class Usuario(models.Model):
    id = models.CharField(max_length=8, verbose_name=u'ID', primary_key=True, blank=True, editable=False)
    def gerar_id(self):
        return ''.join(random.choices('0123456789', k=8))
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.gerar_id()
        super().save(*args, **kwargs)
    nome = models.CharField(max_length=30, verbose_name=u'Nome')
    GENERO = [('M', 'Masculino'),
              ('F', 'Feminino'),
              ('Transgênero', 'Transgênero'),
              ('Não binário', 'Não binário'),
        ]
    genero = models.CharField(max_length=11, verbose_name=u'Gênero', choices=GENERO)
    senha = models.CharField(max_length=20, verbose_name=u'Senha', unique=True)
    cpf = models.CharField(max_length=11, verbose_name=u'CPF', unique=True)
    email = models.EmailField(max_length=40,verbose_name=u'Email')
    telefone = models.CharField(max_length=9, verbose_name=u'Telefone', null=True, blank=True)
    data_nascimento = models.DateField(verbose_name=u'Data de nascimento')

    def __str__(self):
        return self.nome
    
class Endereco(models.Model):
    id = models.CharField(max_length=5, verbose_name=u'ID', primary_key=True, blank=True, editable=False)
    def gerar_id(self):
        return ''.join(random.choices('0123456789', k=5))
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.gerar_id()
        super().save(*args, **kwargs)
    UF = [('AL', 'Alagoas'),
          ('AC','Acre'),
          ('AP','Amapá'),
          ('AM','Amazonas'),
          ('BA','Bahia'),
          ('CE', 'Ceará')
        ]
    uf = models.CharField(max_length=2, verbose_name=u'UF', choices=UF)
    cidade = models.CharField(max_length=29, verbose_name=u'Cidade')
    bairro = models.CharField(max_length=50, verbose_name=u'Bairro')
    rua = models.CharField(max_length=50, verbose_name=u'Rua')
    n = models.CharField(max_length=10, verbose_name=u'N°')
    complemento = models.CharField(max_length=100, verbose_name=u'Complemento(opcional)', null=True, blank=True)
    cliente_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.cliente_id