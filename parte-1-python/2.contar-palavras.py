# Crie uma função que receba uma string e retorne o número de palavras, desconsiderando pontuação.
import string

def contador(texto):
    sem_pontucao = ''.join(x for x in texto if x not in string.punctuation) # Remove os caracteres especiais da string.
    palavras = sem_pontucao.split() # Divide a string em partes separadas por espaços(palavras).
    quantidade = len(palavras) # Conta quantas palavras existem na string
    return quantidade

mensagem = 'Django, é muito bom!'
print(contador(mensagem))
