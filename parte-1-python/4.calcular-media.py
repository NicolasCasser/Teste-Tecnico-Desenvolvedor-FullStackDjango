# Receba um dicionário com nomes e notas e retorne a média das notas.
notas = {"Ana": 8.5, "Bruno": 7.0, "Carlos": 9.0}
total = sum(notas.values()) # Soma as notas dos alunos
quantidade_alunos = len(notas) # Registra a quantidade de alunos presentes dentro do dicionário
media = total / quantidade_alunos 

print('A média dos alunos foi: {:.2f}'.format(media))