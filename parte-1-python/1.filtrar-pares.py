# Crie uma função que receba uma lista de números e retorne apenas os números pares utilizando list comprehension.
lista = [1, 2, 3, 4, 5, 6]

def retorna_pares(lista):
    pares = [x for x in lista if x % 2 == 0]
    return pares

