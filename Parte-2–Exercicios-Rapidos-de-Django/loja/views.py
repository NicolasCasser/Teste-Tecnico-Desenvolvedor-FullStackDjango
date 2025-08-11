from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all() # Pega todos os produtos do banco
    return render(request, 'lista_produtos.html', {'produtos': produtos}) # Passa os dados dos produtos para o template
