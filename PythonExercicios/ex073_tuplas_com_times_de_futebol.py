'''
DESAFIO 073

Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:
    - A) Apenas os 5 primeiros colocados.
    - B) Os últimos 4 colocados da tabela.
    - C) Uma lista com os times em ordem alfabética
    - D) Em que posição na tabela está o time do Athletico-PR.
'''

print(f'{"Tabela do Campeonato Brasileiro de Futebol":41}')
times = ('Palmeiras', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Grêmio', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'São Paulo', 'Fortaleza', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Santos', 'Vasco da Gama', 'Bahia', 'Goiás', 'Coritiba', 'América-MG')
print(f'A) Os 5 primeiros colocados: {times[0:5]}')
print(f'B) Os últimos 4 colocados: {times[16:]}')
print(f'C) Ordem alfabética: {sorted(times)}')
for c in range(0, len(times)):
        if times[c] == 'Athletico-PR':
            print(f'D) Athletico-PR está na {c+1}° posição da tabela')
