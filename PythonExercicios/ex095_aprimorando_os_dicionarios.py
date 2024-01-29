'''
DESAFIO 095

Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.
'''
time = list()
jogador = dict()
partidas = list()
print(f'{"Cadastro de jogador de Futebol":^41}')
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).upper()
        if continuar in 'SN':
            break
        print('ERRO! Responda apenass com S ou N.')
    if continuar == 'N':
        break
print('-' * 41)
print(f'{"cod":^4} ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 41)
for k, v in enumerate(time):
    print(f'{k + 1:^4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 41)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para sair]: ')) - 1
    if busca == 998:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca + 1}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
        print('-' * 41)
