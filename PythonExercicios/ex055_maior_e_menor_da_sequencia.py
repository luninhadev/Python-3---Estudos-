'''
DESAFIO 055

Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lidos.
'''

print('{:^52}'.format('Maior e menor peso de um grupo'))
numeros = ['', '', '', '', '']

for c in range(0, 5):
    n = float(input('Digite o peso da {}° pessoa: '.format(c+1)))
    numeros[c] = n
maior = numeros[0]
menor = numeros[0]

for c in range(0, 5):
    if numeros[c] > maior:
        maior = numeros[c]
    if numeros[c] < menor:
        menor = numeros[c]

print('O maior peso é {}Kg\nO menor peso é {}Kg'.format(maior, menor))
