# DESAFIO 019

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

print('-' * 8, 'Sorteio para apagar o quadro', '-' * 8)

a1 = input('Digite o nome do 1° aluno: ')
a2 = input('Digite o nome do 2° aluno: ')
a3 = input('Digite o nome do 3° aluno: ')
a4 = input('Digite o nome do 4° aluno: ')

lista = [a1, a2, a3, a4]

print('O aluno sorteado é: {}'.format(choice(lista)))