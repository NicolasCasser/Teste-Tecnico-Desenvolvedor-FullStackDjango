# Receba uma lista de dicionários e agrupe os produtos por categoria, contando quantos há em cada.
from pprint import pprint # Biblioteca que exibe dados de forma mais legível 

produtos = [
    {"nome": "Mouse", "Categoria": "Periféricos"},
    {"nome": "Teclado", "Categoria": "Periféricos"},
    {"nome": "Monitor", "Categoria": "Monitores"},
]

# Dicionário que vai armazenar as categoria 
categoria = {}

for i in produtos:
    categoria_produto = i["Categoria"]
    nome_produto = i["nome"]
    
    # Verifica se a categoria já existe no dicionário
    if categoria_produto not in categoria:
        # Se não existir cria a categoria com a lista de itens e a quantidade inicial
        categoria[categoria_produto] = {"itens": [nome_produto], "quantidade": 1}
   
    else:
        # Se já existir apenas adiciona o iten na lista e aumenta a quantidade
        categoria[categoria_produto] ["itens"].append(nome_produto)
        categoria[categoria_produto] ["quantidade"] += 1

pprint(categoria)