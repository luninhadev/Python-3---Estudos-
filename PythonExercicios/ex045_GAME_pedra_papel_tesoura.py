'''
DESAFIO 045

Crie um programa que faça o computador jogar jokenpô com você.
'''

from time import sleep
from random import choice

jkp = ['\U0000270A', '\U0001F590', '\U0000270C']

print('{:=^52}'.format('>>>\033[1m JOKEMPÔ \033[m<<<'))
print('\n')
print('{:^45}'.format('Quer jogar comigo?'))
print('\n')
print('{:^45}'.format('Selecione uma opção:'))
print('{:^45}'.format('[ 1 ] - Pedra.'))
print('{:^45}'.format('[ 2 ] - Papel.'))
print('{:^45}'.format('[ 3 ] - Tesoura.'))

user = int(input('\nDigite um número: '))
print('\n')
pc = choice(jkp)

if user == 1:
    user = '\U0000270A'
elif user == 2:
    user = '\U0001F590'
elif user == 3:
    user = '\U0000270C'

if (user == '\U0000270A') or (user == '\U0001F590') or (user == '\U0000270C'):
    if user != pc:
        if (user == '\U0000270A') and (pc != '\U0001F590') or (pc == '\U0000270A') and (user != '\U0001F590'):
            if user == '\U0000270A':
                print('{:^45}'.format('JO...')), sleep(0.8)
                print('{:^45}'.format('KEM...')), sleep(0.8)
                print('{:^45}'.format('PÔ!!!')), sleep(0.8)
                print('\n')
                print('{:^64}'.format('\033[34mUsuário ->\033[m {} vs {} \033[36m<- Computador\033[m'.format(user, pc)))
                print('{:^54}'.format('Você \033[1;32mVENCEU!\033[m'))
            elif pc == '\U0000270A':
                print('{:^45}'.format('JO...')), sleep(0.8)
                print('{:^45}'.format('KEM...')), sleep(0.8)
                print('{:^45}'.format('PÔ!!!')), sleep(0.8)
                print('\n')
                print('{:^64}'.format('\033[34mUsuário ->\033[m {} vs {} \033[36m<- Computador\033[m'.format(user, pc)))
                print('{:^54}'.format('Você \033[1;31mPERDEU!\033[m'))
        elif (user == '\U0001F590') and ( pc != '\U0000270C') or (pc == '\U0001F590') and ( user != '\U0000270C'):
            if user == '\U0001F590':
                print('{:^45}'.format('JO...')), sleep(0.8)
                print('{:^45}'.format('KEM...')), sleep(0.8)
                print('{:^45}'.format('PÔ!!!')), sleep(0.8)
                print('\n')
                print('{:^64}'.format('\033[34mUsuário ->\033[m {} vs {} \033[36m<- Computador\033[m'.format(user, pc)))
                print('{:^54}'.format('Você \033[1;32mVENCEU!\033[m!'))
            elif pc == '\U0001F590':
                print('{:^45}'.format('JO...')), sleep(0.8)
                print('{:^45}'.format('KEM...')), sleep(0.8)
                print('{:^45}'.format('PÔ!!!')), sleep(0.8)
                print('\n')
                print('{:^64}'.format('\033[34mUsuário ->\033[m {} vs {} \033[36m<- Computador\033[m'.format(user, pc)))
                print('{:^54}'.format('Você \033[1;31mPERDEU!\033[m'))
        elif (user == '\U0000270C') and (pc != '\U0000270A') or (pc == '\U0000270C') and (user != '\U0000270A'):
            if user == '\U0000270C':
                print('{:^45}'.format('JO...')), sleep(0.8)
                print('{:^45}'.format('KEM...')), sleep(0.8)
                print('{:^45}'.format('PÔ!!!')), sleep(0.8)
                print('\n')
                print('{:^64}'.format('\033[34mUsuário ->\033[m {} vs {} \033[36m<- Computador\033[m'.format(user, pc)))
                print('{:^54}'.format('Você \033[1;32mVENCEU!\033[m!'))
            elif pc == '\U0000270C':
                print('{:^45}'.format('JO...')), sleep(0.8)
                print('{:^45}'.format('KEM...')), sleep(0.8)
                print('{:^45}'.format('PÔ!!!')), sleep(0.8)
                print('\n')
                print('{:^64}'.format('\033[34mUsuário ->\033[m {} vs {} \033[36m<- Computador\033[m'.format(user, pc)))
                print('{:^54}'.format('Você \033[1;31mPERDEU!\033[m'))
    elif user == pc:
        print('{:^45}'.format('JO...')), sleep(0.8)
        print('{:^45}'.format('KEM...')), sleep(0.8)
        print('{:^45}'.format('PÔ!!!')), sleep(0.8)
        print('\n')
        print('{:^64}'.format('\033[34mUsuário ->\033[m {} vs {} \033[36m<- Computador\033[m'.format(user, pc,)))
        print('{:^54}'.format('\033[1;33mEMPATE!!!\033[m'))
else:
    print('\033[1;31mDigite um número válido!\033[m')
print('{:_^45}'.format(''))
