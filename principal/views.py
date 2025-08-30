from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'html/perfil.html')

def er404(request):
    return render(request, 'html/er404.html')

def er403(request):
    return render(request, 'html/er403.html')

def er500(request):
    return render(request, 'html/er500.html')