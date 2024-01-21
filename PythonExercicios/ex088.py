'''
DESAFIO 088

Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo., cadastrando tudo em uma lista composta.
'''
from random import randint
from time import sleep
jogos = list()
jogo = list()
print(f'=' * 41)
print(f'{"JOGO DA SORTE":^41}')
print(f'=' * 41)
n = int(input('\nQuantos jogos serão sorteados?: '))
tot = 1
while tot <= n:
    cont = 0
    while True:
        num = randint(1, 60)
        if n not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(jogo[:])
    jogo.clear()
    tot += 1
print(f'\n{f"SORTEANDO {n} JOGOS":-^41}')
for c in range(n):
    print(f'Jogo {c + 1}: {jogos[c]}')
    sleep(1)
print(f'\n{f"BOA SORTE!":-^41}')