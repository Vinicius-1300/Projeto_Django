from .models import Usuario
from functools import wraps 
from django.shortcuts import redirect
from django.http import HttpResponse

def usuario_requisicao(nivel=None):
    def decorador(view_function):
        @wraps(view_function)
        def _wrapped_view(request, *args, **kwargs):
            usuario_sessao = request.session.get('id')
            if not usuario_sessao:
                return redirect('403')
            try:
                user = Usuario.objects.get(id=usuario_sessao)
                if nivel and user.nivel != nivel:
                    return HttpResponse('Acesso negado')
                request.user = user
            except Usuario.DoesNotExist:
                return redirect('403')
            return view_function(request, *args, **kwargs)
        return _wrapped_view
    return decorador