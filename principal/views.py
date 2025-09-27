from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Usuario
from .forms import Cadastro

def index(request):
    return render(request, 'html/index.html')

def login(request):
    erro = None
    if request.method == 'POST':
        email = request.POST.get('email') 
        senha = request.POST.get('senha')
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth_admin = authenticate(request, username=username, password=password)
        if auth_admin:
            if auth_admin.is_superuser:
                return redirect('admin')
        auth_usuario = Usuario.objects.filter(email=email, senha=senha).first()
        if auth_usuario:
            request.session['id'] = auth_usuario.id
            return redirect('index') 
        erro = 'Email ou senha inválidos'
    return render(request, 'html/login.html', {'erro': erro})

def cadastro(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Cadastro()
    return render(request, 'html/cadastro.html', {'form': form})

def recuperar_senha(request):
    return render(request, 'html/rec_senha.html')

def alterar_senha(request):
    return render(request, 'html/alterar_senha.html')

def perfil(request):
    return render(request, 'html/perfil.html')

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