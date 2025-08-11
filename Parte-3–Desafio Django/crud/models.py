from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) # Cada pedido é ligado a um cliente, se o cliente for apagado, seus pedidos também serão
    produtos = models.ManyToManyField(Produto) # O pedido pode ter vários produtos e cada produto pode estar em vários pedidos
    data = models.DateField(auto_now_add=True) # Guarda a data que o pedido foi criado 

    # Retorna uma mensagem com o número do pedido(id) e o nome do cliente
    def __str__(self):
        return (f"Pedido: {self.id} - {self.cliente.nome}")
    
    # Calcula o valor total do pedido
    def valor_total(self):
        return sum(produto.preco for produto in self.produtos.all()) # Traz todos os produtos relacionados ao pedido e soma os preços de cada um.
