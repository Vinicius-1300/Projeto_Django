from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Usuario
#from .models import Member

def index(request):
    return render(request, 'html/index.html')

def login(request):
    return render(request, 'html/login.html')

def cadastro(request):
    return render(request, 'html/cadastro.html')

def recuperar_senha(request):
    return render(request, 'html/rec_senha.html')

def alterar_senha(request):
    return render(request, 'html/alterar_senha.html')

def perfil(request):
    dados = Usuario.objects.all()
    return render(request, 'html/perfil.html', {'dados': dados})

def er404(request):
    return render(request, 'html/er404.html')

def er403(request):
    return render(request, 'html/er403.html')

def er500(request):
    return render(request, 'html/er500.html')

#Request dos dados no model

"""def dados(request):
    dado = Pessoa.objects.all().values()
    template = loader.get_template('html/perfil.html')
    context = {
        'dados': dado,
    }
    return HttpResponse(template.render(context, request))
    #Alternativa: return render(request, 'html/perfil.html', {'dados': dado})"""