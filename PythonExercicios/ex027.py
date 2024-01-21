'''
DESAFIO 027

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''

print('-' * 8, 'Fatiando nomes', '-' * 8)

nome = input('Digite seu nome completo: ')

# fatia o nome em lista
listnome = nome.split()
prinome = listnome[0]

# Verifica a quantidade de letras que tem o primeiro nome e acrescenta o espaço entre o primeiro e segundo nome
quantprinome = len(listnome[0]) + 1

# Junta a lista como se fosse um nome só
listnome = ' '.join(listnome)

# Atribui ao segundo nome o resto do nome apartir do tamanho do primeiro nome
segnome = listnome[quantprinome:]

print('Seu nome é: {}\nPrimeiro nome é: {}\nSegundo nome é: {}'.format(nome, prinome, segnome))
