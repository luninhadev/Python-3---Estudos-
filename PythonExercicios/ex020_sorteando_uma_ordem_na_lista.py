# DESAFIO 020

# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

print('-' * 8, 'Sorteio de trabalhos', '-' * 8)

a1 = input('Digite o nome do 1° aluno: ')
a2 = input('Digite o nome do 2° aluno: ')
a3 = input('Digite o nome do 3° aluno: ')
a4 = input('Digite o nome do 4° aluno: ')

lista: list[str] = [a1, a2, a3, a4]
shuffle(lista)

print('Os nomes sorteados foram\n1° {}\n2° {}\n3° {}\n4° {}'.format(lista[0], lista[1], lista[2], lista[3]))
