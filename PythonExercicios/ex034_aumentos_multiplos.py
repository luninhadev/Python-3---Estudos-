'''
DESAFIO 034

Escreva um programa que escreva o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1250,00 calcule um aumento de 10%.
Para os salários inferiores ou iguais, o aumento é de 15%
'''

print('-' * 8, 'Calculo de salários', '-' * 8)

s = int(input('Digite seu salário: '))

if s < 1250:
    aumento = s * 0.15
    print('Seu aumento foi de 15%, resultando em: R${:.2f}'.format(aumento))
else:
    aumento = s * 0.1
    print('Seu aumento foi de 10%, resultando em: R${:.2f}'. format(aumento))
