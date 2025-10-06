from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from .models import Usuario
from .forms import Cadastro

def index(request):
    return render(request, 'html/index.html')

def login(request):
    erro = None
    if request.method == 'POST':
        email = request.POST.get('email') 
        senha = request.POST.get('senha')
        auth_usuario = Usuario.objects.filter(email=email).first()
        if auth_usuario:
            request.session['id'] = auth_usuario.id
            if auth_usuario.nivel == 'Padrão':
                print("Usuário autenticado:", auth_usuario.email)
                print("Nível:", auth_usuario.nivel)
                return redirect('index')
            elif auth_usuario.nivel == 'Gestor':
                print("Usuário autenticado:", auth_usuario.email)
                print("Nível:", auth_usuario.nivel)
                return redirect('gestor')
        erro = 'Eamil ou senha inválidos'

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
    user_id = request.session.get('id')
    if not user_id:
        return redirect('login')
    dados = Usuario.objects.get(id=user_id)
    return render(request, 'html/perfil.html', {'dados': dados})

def er404(request):
    return render(request, 'html/er404.html')

def er403(request):
    return render(request, 'html/er403.html')

def er500(request):
    return render(request, 'html/er500.html')

def gestor_page(request):
    return render(request, 'html/gestor_page.html')