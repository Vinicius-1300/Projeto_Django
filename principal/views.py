from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Usuario
from .forms import Cadastro, Endereco

def index(request):
    return render(request, 'html/index.html')

def login(request):
    return render(request, 'html/login.html')

def cadastro(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
        form_endereco = Endereco(request.POST)
        if form.is_valid() and form_endereco.is_valid():
            form.save()
            form_endereco.save()
            return redirect('login')
    else:
        form = Cadastro()
        form_endereco = Endereco()
    return render(request, 'html/cadastro.html', {'form': form, 'form_endereco': form_endereco})

def recuperar_senha(request):
    return render(request, 'html/rec_senha.html')

def alterar_senha(request):
    return render(request, 'html/alterar_senha.html')

def perfil(request):
    dados = get_object_or_404(Usuario, pk=request.user.id)
    form = Cadastro(instance=dados)
    if(request.method == 'POST'):
        form = Cadastro(request.POST, instance=dados)
        if(form.is_valid()):
            form.save()
            return redirect('index')
        else:
            return render(request, 'html/perfil.html', {'dados': dados, 'form':form})
    else:
         return render(request, 'html/perfil.html', {'dados': dados, 'form':form})

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