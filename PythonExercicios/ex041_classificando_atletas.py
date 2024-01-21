'''
    DESAFIO 041

A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
    - Até 9 anos: Mirim.
    - Até 14 anos: Infantil.
    - Até 19 anos: Júnior.
    - Até 20 anos: Sênior.
    - Acima: Master.
'''
from datetime import date

print('-' * 8, 'Confederação Nacional de Natação', '-' * 8)

nasc = int(input('Digite o ano que você nasceu: '))
idade = date.today().year - nasc

if idade <= 9:
    print('Sua categoria é: MIRIM.')
elif idade <= 14:
    print('Sua categoria é: INFANTIL.')
elif idade <= 19:
    print('Sua categoria é: JÚNIOR.')
elif idade == 20:
    print('Sua categoria é: SÊNIOR.')
elif idade > 20:
    print('Sua categoria é: MASTER.')
