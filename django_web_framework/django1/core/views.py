from django.shortcuts import render
from .models import Produto

from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader


def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é demais!',
        'produtos': produtos,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    # print(f'PK: {pk}')
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod,
    }
    return render(request, 'produto.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)


def sobre(request):
    return render(request, 'sobre.html')

'''
def index(request):
    if str(request.user) == "AnonymousUser":
        teste = "Usuário não logado"
    else:
        teste = "Usuário logado"
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é demais!',
        'logado': teste,
    }
    return render(request, 'index.html', context)
'''