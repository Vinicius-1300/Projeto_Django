from django.db import models
class Usuario(models.Model):
    nome = models.CharField(max_length=255, verbose_name=u'Nome')
    senha = models.CharField(max_length=20, verbose_name=u'Senha')
    cpf = models.CharField(max_length=15, verbose_name=u'CPF')
    email = models.EmailField(verbose_name=u'Email')
    telefone = models.CharField(max_length=30, verbose_name=u'Telefone', null=True, blank=True)
    data_nascimento = models.DateField(verbose_name=u'Data de nascimento')
    UF = [('AL', 'Alagoas'),
          ('AC','Acre'),
          ('AP','Amapá'),
          ('AM','Amazonas'),
          ('BA','Bahia'),
        ]
    uf = models.CharField(max_length=2, verbose_name=u'UF', choices=UF)

    def __str__(self):
        return self.nome