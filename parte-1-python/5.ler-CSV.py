# Leia um arquivo CSV com colunas nome, categoria, preco e retorne um dicionário agrupando os produtos por categoria com o preço total de cada uma.
import csv # Biblioteca para manipular os dados em arquivos csv 

categorias = {} # Dicionário onde será armazenado o preço total das categorias

# Abre o arquivo.csv
with open("produtos.csv", newline='') as arquivo:
    leitor = csv.DictReader(arquivo) # Lê cada linha do csv como um dicionário utilizando o nome das colunas como chaves
     
    for linha in leitor:
        categoria = linha["categoria"] # Pega o texto da categoria
        preco = float(linha["preco"]) # Converte os preços para float
        
        if categoria not in categorias:
            categorias[categoria] = preco # Se a categoria não existe, cria ela com o valor do preço.
        else:
            categorias[categoria] += preco # Se já existe apenas soma o valor 

print(categorias)