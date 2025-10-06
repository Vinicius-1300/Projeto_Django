from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('rec_senha/', views.recuperar_senha, name='rec_senha'),
    path('alterar_senha/', views.alterar_senha, name='alterar_senha'),
    path('perfil/', views.perfil, name='perfil'),
    path('404', views.er404, name='404'),
    path('403', views.er403, name='403'),
    path('500', views.er500, name='500'),
    path('gestor/', views.gestor_page, name='gestor')
]
