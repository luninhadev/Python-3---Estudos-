'''
DESAFIO 022

Crie um programa que leia o nome completo de uma pessoa e mostre:
 - O nome com todas as letras maiúsculas.
 - O nome com todas minúsculas.
 - Quantas letras ao todo (sem considerar os espaços).
 - Quantas letras tem o primeiro nome.
'''

nome = input('Digite seu nome completo: ')

maiusc = nome.upper()
minusc = nome.lower()
qtdletras = nome.split()
qtdletras = len(''.join(qtdletras))
letras = nome.split()

print('Seu nome: {}\nEm maiúscula: {}\nEm minúscula: {}\nQuantidade de letras: {}\nO primeiro nome tem: {} letras'.format(nome, maiusc, minusc, qtdletras,len(letras[0])))

