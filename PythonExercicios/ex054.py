'''
DESAFIO 054

Crie um programa que leia o ano de nascimento de 7 pessoas. No final mostre qunatas pessoas não atingiram a maioridade
e quantas já são maiores, considerando a maioridade 21 anos.
'''
from datetime import date

print('{:^52}'.format('Verificando idade de um grupo'))

maioridade = 0
menoridade = 0

for c in range(1, 8):
    anonasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    anoatual = date.today().year

    if (anoatual - anonasc) >= 21:
        maioridade += 1
    elif (anoatual - anonasc) <= 20:
        menoridade += 1
print('{} pessoas são maior de idade.\n{} ainda são menores.'.format(maioridade, menoridade))
