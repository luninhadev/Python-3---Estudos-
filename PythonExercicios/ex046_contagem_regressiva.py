'''
DESAFIO 046

Faça um progama que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de
10 até 0 com uma pausa de  sesgundo entre eles.
'''

from time import sleep

print('{:_^45}'.format('Contagem regressiva'))

for c in range(10, -1, -1):
    if c > 1:
        print(c, 'segundos')
        sleep(1)
    elif (c == 1) or (c == 0):
        print(c, 'segundo')
        sleep(1)
    else:
        print(c, 'segundos')
        sleep(1)
    