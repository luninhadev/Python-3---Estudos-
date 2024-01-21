'''
DESAFIO 051

Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros termo dessa
progressão.
'''

print('{:=^52}'.format('Progressão Aritmética'))

termo1 = int(input('Digite o 1° termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
decimo = termo1 + (10 - 1) * razao

print('Os 10 termos dessa P.A. são:')

for c in range(termo1, decimo + razao, razao):
    print('[{}]'.format(c), end=' ')
