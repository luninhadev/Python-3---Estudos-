'''
DESAFIO 032

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''

from datetime import date

print('-' * 8, 'Verificando se o ano é bissexto', '-' * 8)

ano = int(input('Que ano que analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('{} é bissexto!'.format(ano))
        else:
            print('{} não é bissexto!'.format(ano))
    else:
        print('{} é bissexto!'.format(ano))
else:
    print('{} não é bissexto!'.format(ano))

'''TAMBÉM FUNCIONA:
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
'''
