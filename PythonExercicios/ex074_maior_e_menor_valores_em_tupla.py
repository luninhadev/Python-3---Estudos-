'''
DESAFIO 074

Crie um programa que vai gerar 5 números aleatórios e colocar em uma Tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na Tupla.
'''
from random import randint
print(f'{"Sorteio de Tupla":^41}')
ncomp = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Números gerado aletóriamente: {ncomp}')
print(f'Maior número: {max(ncomp)}\nMenor número: {min(ncomp)}')
