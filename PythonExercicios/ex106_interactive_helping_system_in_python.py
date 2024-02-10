'''
DESAFIO 106

Faça um mini sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palara "FIM", o programa se encerrará.
OBS: Use cores.
'''
from time import sleep
c = ('\033[m',          # 0 - Sem cores
     '\033[0;30;41m',   # 1 - Vermelho
     '\033[0;30;42m',   # 2 - Verde
     '\033[0;30;43m',   # 3 - Amarelo
     '\033[0;30;44m',   # 4 - Azul
     '\033[0;30;45m',   # 5 - Roxo
     '\033[0;30;46m')   # 6 - Branco


def funbi(com):
    print(f'\033[34;30;43m{"-" * 41:^41}\033[m')
    print(f'\033[34;30;43m{"Acessando manual do comando...":^41}\033[m')
    print(f'\033[34;30;43m{"-" * 41:^41}\033[m')
    sleep(2)
    print(f'\033[0;30;42m')
    help(com)
    print('\033[m')

def titulo1(msg, cor=0):
    tam = len(msg)
    print(f'\033[34;30;44m{"-" * 41:^41}\033[m')
    print(f'\033[34;0;44m{msg:^41}\033[m')
    print(f'\033[34;30;44m{"-" * 41:^41}\033[m')


def titulo2(msg, cor=0):
    tam = len(msg)
    print(f'\033[34;30;41m{"-" * 41:^41}\033[m')
    print(f'\033[34;0;41m{msg:^41}\033[m')
    print(f'\033[34;30;41m{"-" * 41:^41}\033[m')

titulo1('SISTEMA DE AJUDA PYHELP')
comando = ''
while True:
    comando = str(input('Função ou Biblioteca >> '))
    if comando.upper() == 'FIM':
        break
    else:
        funbi(comando)
titulo2('ATÉ LOGO')
