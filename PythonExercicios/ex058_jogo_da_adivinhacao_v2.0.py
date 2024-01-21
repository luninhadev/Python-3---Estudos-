'''
DESAFIO 058

Melhore o jogo, onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer
'''

from random import randint
from time import sleep

print('\033[1;33m-=-\033[m' * 18)
print('  \033[1mVou pensar em um número... Você consegue acertar?\033[m  ')
print('\033[1;33m-=-\033[m' * 18, '\n')
ncomp = int(randint(0, 10))
print('Okay, já pensei em um número de 0 a 5.')
nuser = int(input('Qual eu pensei: '))

print('\033[1mPROCESSANDO...\033[m\n')
sleep(2)
palpites = 0

while nuser != ncomp:
    ncomp = int(randint(0, 5))
    nuser = int(input('\033[1mPERDEU!!!\033[m Eu levo a vitória dessa vez... Tente de novo: '))
    palpites += 1
    if nuser == ncomp:
        print('\033[1mPARABÉNS!!!\033[m Você me venceu, eu pensei no número {}!'.format(nuser))
        print('Foram necessários {} palpites'.format(palpites))
