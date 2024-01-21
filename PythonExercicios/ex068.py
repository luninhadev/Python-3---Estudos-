'''
DESAFIO 068

Faça um programa que jogue Par ou Ímpar com o computador. O jogo só será interrompido quando o jogador PERDER
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
print(f'{"":=^45}')
print(f'{"PAR ou ÍMPAR":^45}')
print(f'{"":=^45}')
n = 0
parimpar = ''
count = 0
while True:
    comp = randint(0, 10)
    n = int(input('Digite um número: '))
    parimpar = str(input('Par ou ímpar? [P/I]: ')).upper()
    while parimpar not in 'PI':
        parimpar = str(input('Par ou ímpar? [P/I]: ')).upper()
    if (n + comp) % 2 == 0:
        print(f'{"":=^45}')
        print(f"{f'Computador -> {comp} vs {n} <- Usuário':^45}")
        print(f'{"":=^45}')
        if parimpar == 'P':
            parimpar = 'PAR'
            print(f"{f'{n + comp} Deu {parimpar} Você ganhou!':^45}")
            print(f'{"":-^45}')
            count += 1
        else:
            parimpar = 'PAR'
            print(f"{f'{n + comp} Deu {parimpar} Você perdeu...':^45}")
            print(f"{f'Total de vitórias consecutivas: {count}':^45}")
            break
    if (n + comp) % 2 != 0:
        print(f'{"":=^45}')
        print(f"{f'Computador -> {comp} vs {n} <- Usuário':^45}")
        print(f'{"":=^45}')
        if parimpar == 'I':
            parimpar = 'ÍMPAR'
            print(f"{f'{n + comp} Deu {parimpar} Você ganhou!':^45}")
            print(f'{"":-^45}')
            count += 1
        else:
            parimpar = 'ÍMPAR'
            print(f"{f'{n + comp} Deu {parimpar} Você perdeu...':^45}")
            print(f"{f'Total de vitórias consecutivas: {count}':^45}")
            break
