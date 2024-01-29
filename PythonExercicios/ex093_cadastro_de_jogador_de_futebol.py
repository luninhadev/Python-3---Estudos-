'''
DESAFIO 093

Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado num dicionário, incluindo o total de gols feitos durante campeonato.
'''
jogador = {'nome': '', 'gols': [], 'total': 0}
print(f'{"Cadastro de jogador de Futebol":^41}')
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['total'] += jogador['gols'][c]
print(f'{"Dados do jogador":-^41}')
print(jogador)
print(f'{"Aproveitamento do jogador":-^41}')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'{"Aproveitamento do Jogador":-^41}')
print(f'{jogador["nome"]} jogou {partidas} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'=> Na partida {i + 1}, fez {v} gols')
print(f'Total de gols: {jogador['total']}')
