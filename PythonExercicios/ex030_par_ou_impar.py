'''
DESAFIO 030

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

print('\033[34m-\033[m' * 8, '\033[31mPAR!\033[m ou \033[34mÍMPAR!\033[m', '\033[31m-\033[m' * 8)
n = int(input('Digite um número inteiro: '))

if n % 2 == 0:
    print('{} é um número \033[31mPAR!\033[m'.format(n))
else:
    print('{} é um número \033[34mÍMPAR!\033[m'.format(n))
