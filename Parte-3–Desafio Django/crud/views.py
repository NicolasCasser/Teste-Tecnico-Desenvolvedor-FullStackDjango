from django.shortcuts import render, redirect
from .models import Cliente, Produto, Pedido

def home(request):
    return render(request, 'home.html')

def lista_clientes(request):
    clientes = Cliente.objects.all() # Pega todos os clientes do banco
    return render(request, 'lista_clientes.html', {'clientes': clientes}) # Renderiza o template com os dados

def criar_cliente(request):
    if request.method == "GET":
        return render(request, 'criar_cliente.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        cliente = Cliente(
            nome=nome,
            email=email,
            telefone=telefone,
        )

        cliente.save()

        return redirect('criar_cliente')

def deletar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('lista_clientes')

def atualizar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    
    cliente.nome = nome
    cliente.email = email
    cliente.telefone = telefone
    cliente.save()
    return redirect('lista_clientes')

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == "GET":
        return render(request, 'criar_produto.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')

        produto = Produto(
            nome=nome,
            preco=preco
        )

        produto.save()

        return redirect('criar_produto')

def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('lista_produtos')

def atualizar_produto(request, id):
    produto = Produto.objects.get(id=id)

    nome = request.POST.get('nome')
    preco = request.POST.get('preco')

    produto.nome = nome
    produto.preco = preco
    produto.save()
    return redirect('lista_produtos')

def criar_pedido(request):
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()

    if request.method == "POST":
        cliente_id = request.POST.get('cliente')
        produtos_id = request.POST.getlist('produtos')

        cliente = Cliente.objects.get(id=cliente_id)
        pedido = Pedido.objects.create(cliente=cliente)

        for pid in produtos_id:
            produto = Produto.objects.get(id=pid)
            pedido.produtos.add(produto)

        return redirect('lista_pedidos')
    
    return render(request, 'criar_pedido.html', {'clientes': clientes, 'produtos': produtos})

def lista_pedidos(request):
    cliente_id = request.GET.get('cliente')
    pedidos = Pedido.objects.all().select_related('cliente').prefetch_related('produtos')

    if cliente_id:
        pedidos = pedidos.filter(cliente__id=cliente_id)

    clientes = Cliente.objects.all()

    return render(request, 'lista_pedidos.html', {'pedidos': pedidos, 'clientes': clientes, 'cliente_selecionado': cliente_id})