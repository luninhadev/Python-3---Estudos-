'''
DESAFIO 053

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''
from time import sleep

print('{:^52}'.format('A frase é um Palíndromo?'))

frase = str(input('Digite uma frase: ')).split()
print('Tirando os espaços em branco...')
sleep(2)

frase1 = ''.join(frase)
invert = frase1[::-1]

print('\nFrase normal: ', frase1)
print('Frase invertida: ', invert)

if frase1 == invert:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo')

'''
Exemplos:
    - apos a sopa
    - a sacada da casa
    - a torre da derrota
    - o lobo ama o bolo
    - anotaram a data da maratona
'''