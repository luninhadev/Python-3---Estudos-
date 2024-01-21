'''
    DESAFIO 038

Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma das
seguintes mensagens:
    - O primeiro valor é maior.
    - O segundo valor é maior.
    - Não existe valor maior os dois são iguais.
'''

print('-' * 8, 'Maior valor', '-' * 8)
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print('O \033[33mprimeiro valor\033[m é \033[34mmaior\033[m')
elif n2 > n1:
    print('O \033[33msegundo valor\033[m é \033[34mmaior\033[m')
else:
    print('\033[33mNão existe\033[m valor maior, os dois são \033[34miguais\033[m')
