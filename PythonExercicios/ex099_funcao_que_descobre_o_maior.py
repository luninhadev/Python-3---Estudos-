'''
DESAFIO 099

Faca um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer dele é maior.
'''
from time import sleep
def maior(lst):
    c = 0
    for i in range(0, randint(0, 10)):
        lista.append(randint(0, 100))
    m = lst[0]
    print(f'-=' * 41)
    print('Analisando os valores passados...')
    for i, n in enumerate(lst):
        sleep(0.5)
        print(f'{n} ', end='')
    print(f'Foram informados {len(lst)} valores ao todo')
    while c < len(lst):
        if m < lst[c]:
            m = lst[c]
        c += 1
    print(f'O maior valor informado foi: {m}.')
    lst.clear()


lista = list()
from random import randint
print(f'{"Função que descobre o maior":^82}')
maior(lista)
maior(lista)
maior(lista)
maior(lista)
maior(lista)
