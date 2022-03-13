from django.urls import path

from .views import index, contato, produto, sobre

urlpatterns = [
    path('', index, name='index'), # se for para a raiz, manda para o index
    path('contato', contato),
    path('produto/<int:pk>', produto, name='produto'),
    path('sobre', sobre, name='sobre')
]