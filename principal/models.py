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
    nome = models.CharField(max_length=255, verbose_name=u'Nome')
    senha = models.CharField(max_length=20, verbose_name=u'Senha', unique=True)
    cpf = models.CharField(max_length=15, verbose_name=u'CPF', unique=True)
    email = models.EmailField(verbose_name=u'Email')
    telefone = models.CharField(max_length=30, verbose_name=u'Telefone', null=True, blank=True)
    data_nascimento = models.DateField(verbose_name=u'Data de nascimento')
    UF = [('AL', 'Alagoas'),
          ('AC','Acre'),
          ('AP','Amapá'),
          ('AM','Amazonas'),
          ('BA','Bahia'),
          ('CE', 'Ceará')
        ]
    uf = models.CharField(max_length=2, verbose_name=u'UF', choices=UF)

    def __str__(self):
        return self.nome