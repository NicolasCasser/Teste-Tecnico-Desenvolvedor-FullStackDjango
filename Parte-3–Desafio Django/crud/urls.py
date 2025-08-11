from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista_clientes/', views.lista_clientes, name="lista_clientes"),
    path('criar_cliente/', views.criar_cliente, name="criar_cliente"),
    path('deletar_cliente/<int:id>', views.deletar_cliente, name="deletar_cliente" ),
    path('atualizar_cliente/<int:id>', views.atualizar_cliente, name="atualizar_cliente"),
    path('lista_produtos/', views.lista_produtos, name="lista_produtos"),
    path('criar_produto/', views.criar_produto, name="criar_produto"),
    path('deletar_produto/<int:id>', views.deletar_produto, name="deletar_produto"),
    path('atualizar_produto/<int:id>', views.atualizar_produto, name="atualizar_produto"),
    path('criar_pedido/', views.criar_pedido, name="criar_pedido"),
    path('lista_pedidos/', views.lista_pedidos, name="lista_pedidos"),
]
