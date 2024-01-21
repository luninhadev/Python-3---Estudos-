'''
    DESAFIO 039

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    - Se ele ainda vai se alistar ao serviço militar.
    - Se é a hora de se alistar.
    - Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date

print('-' * 8, 'Alistamento militar', '-' * 8)

nasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nasc

if idade < 18 and 18 - idade == 1:
    print('Você não completou 18 anos, falta {} ano para se alistar.'.format(18 - idade))
elif idade < 18 and 18 - idade > 1:
    print('Você não completou 18 anos, falta {} anos para se alistar.'.format(18 - idade))
elif idade == 18 and 18 - idade == 0:
    print('Você completou 18 anos!!! Está na hora de se alistar!!!')
elif idade > 18 and idade - 18 == 1:
    print('Você já tem mais de 18 anos, passou {} ano do alistamento.'.format(idade - 18))
elif idade > 18 and idade - 18 > 1:
    print('Você ja tem mais de 18 anos, passou {} anos do alistamento.'.format(idade - 18))
