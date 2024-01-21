'''
DESAFIO 052

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

print('{:^52}'.format('Números primos'))

n = int(input('Digite um número inteiro: '))
mult = 0

for c in range(1, n+1):
    if n % c == 0:
        print('Múltiplo de {}'.format(c))
        mult += 1
if mult == 2:
    print('{} é primo.'.format(n))
else:
    print('{} não é primo.'.format(n))
