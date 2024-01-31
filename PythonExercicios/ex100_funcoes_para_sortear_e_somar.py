'''
DESAFIO 100

Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira
função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
os valores PARES sorteados pela função anterior
'''
from random import randint
from time import sleep
def sorteia(lst1):
    for c in range(0, 5):
        lst1.append(randint(0, 10))
    print(f'Sorteando valores da lista: ', end='')
    for c in range(0, 5):
        sleep(0.5)
        print(f'{lst1[c]} ', end='')
    print('PRONTO!')
    return lst1


def somaPar(lst2):
    par = 0
    for c in range(0, len(lst2)):
        if lst2[c] % 2 == 0:
            par += lst2[c]
    print(f'Somando os valores pares de ', end='')
    for c in range(0, len(lst2)):
        sleep(0.5)
        print(f'{lst2[c]} ', end='')
    print(f'temos {par}')


lista = list()
print(f'{"Funções para sortear e somar":^41}')
sorteia(lista)
somaPar(lista)
