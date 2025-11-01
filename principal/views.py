from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from .models import Usuario
from .forms import Cadastro, Endereco
from .decorador import usuario_requisicao
import bcrypt

@usuario_requisicao()
def index(request):
    return render(request, 'html/index.html')

def login(request):
    erro = None
    if request.method == 'POST':
        email = request.POST.get('email') 
        senha = request.POST.get('senha')
        auth_usuario = Usuario.objects.filter(email=email).first()
        if auth_usuario and bcrypt.checkpw(senha.encode('utf-8'), auth_usuario.senha.encode('utf-8')):
            request.session['id'] = auth_usuario.id
            if auth_usuario.nivel == 'Padrão':
                return redirect('index')
            elif auth_usuario.nivel == 'Gestor':
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

@usuario_requisicao()
def cadastroEndereco(request):
   return render(request, 'html/cadastro_endereco')
   """def cadastroEndereco(request):
    if request.method == 'POST':
        form_end = Endereco(request.POST)
        if form_end.is_valid():
            endereco = form_end.save(commit=False)
            if isinstance(request.user, Usuario):
                endereco.cliente_id = request.user  
                endereco.save()
                return redirect('index')
            else:
                form_end.add_error(None, 'Usuário não está autenticado ou não é válido.')
    else:
        form_end = Endereco()
    return render(request, 'html/cadastro_endereco.html', {
        'form_end': form_end
    })"""

def recuperar_senha(request):
    return render(request, 'html/rec_senha.html')

def alterar_senha(request):
    return render(request, 'html/alterar_senha.html')

@usuario_requisicao()
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

@usuario_requisicao(nivel='Gestor')
def gestor_page(request):
    return render(request, 'html/gestor_page.html')

@usuario_requisicao()
def logout_sessao(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Você saiu com sucesso!")
    return redirect('login')

@usuario_requisicao()
def edicao_dados(request, id):
    edicao = get_object_or_404(Usuario, pk=id)
    form = Cadastro(instance=edicao)
    if request.method == 'POST':
        form = Cadastro(request.POST, instance=edicao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados atualizados com sucesso')
            return redirect('login')
        else:
            messages.error(request, 'Erro na alteração dos dados, verifique se foram alterados corretamente')
            return render(request, 'html/edicao_dados.html', {'form': form, 'edicao': edicao})
    else:
        return render(request, 'html/edicao_dados.html', {'form': form, 'edicao': edicao})
    
@usuario_requisicao()
def deletar_conta(request, id):
    deletar = get_object_or_404(Usuario, pk=id)
    deletar.delete()
    messages.success(request, 'Conta excluida com sucesso')
    return redirect('login')