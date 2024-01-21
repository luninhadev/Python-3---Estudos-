'''
DESAFIO 049

Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, so que utilizando um laço for.
'''

print('TABUADA')
n = int(input('Digite um número inteiro: '))

for i in range(11):
    print('{} x {} = {}'.format(n, i, n * i))
