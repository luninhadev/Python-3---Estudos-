'''
DESAFIO 028

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep

print('\033[1;33m-=-\033[m' * 18)
print('  \033[1mVou pensar em um número... Você consegue acertar?\033[m  ')
print('\033[1;33m-=-\033[m' * 18, '\n')
ncomp = int(randint(0, 5))
print('Okay, já pensei em um número de 0 a 5.')
nuser = int(input('Qual eu pensei: '))

print('\033[1mPROCESSANDO...\033[m\n')
sleep(2)

if nuser == ncomp:
    print('\033[1mPARABÉNS!!!\033[m Você me venceu, eu pensei no número {}!'.format(nuser))
else:
    print('\033[1mPERDEU!!!\033[m Você é bom, mas eu levo a vitória dessa vez...')
