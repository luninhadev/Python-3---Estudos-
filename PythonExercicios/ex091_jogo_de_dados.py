'''
DESAFIO 091

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número do dado.
'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = list()
print(f'{"Valores Sorteado":-^41}')
for k, v in jogo.items():
    print(f'{k} tirou o {v} no dado')
    sleep(1)
print(f'{"RANKING DO JOGADORES":-^41}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1} lugar --> {v[0]} dado: {v[1]}')
    sleep(1)
