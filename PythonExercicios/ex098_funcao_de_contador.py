'''
DESAFIO
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e
realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
    a)De 1 até 10, de 1 em 1
    b)de 10 até 0, de 2 em 2
    C)Uma contagem personalizada
'''
from time import sleep
def contador(inicio, fim, passo):
    i = inicio
    if inicio <= fim:
        if passo == 0:
            passo = 1
        while i < fim + 1:
            sleep(0.5)
            print(f'{i} ', end='')
            i += passo
        print('FIM!')
    elif inicio > fim:
        if passo < 0:
            passo = passo * -1
        if passo == 0:
            passo = 3 - 2
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        while i >= fim:
            sleep(0.5)
            print(f'{i} ', end='')
            i -= passo
        print('FIM!')


print(f'{"Contador":^41}')
print('-' * 41)
print('Contagem de 1 até 10 de 1 em 1:')
contador(1, 10, 1)
print('-' * 41)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
pas = int(input('Digite o passo: '))
print('-' * 41)
contador(ini, f, pas)
