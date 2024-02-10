'''
DESAFIO 103

Crie um programa que tenha a função chamada ficha(), que receba dois parâmetros opcionai: o nome de um jogador
e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
'''
def ficha(n, t):
    '''
    -> Vai verificar se foram preenchidos, vai preencher e mostrar o resultado.
    :param n: nome
    :param t: total de gols
    Função criada por Luna Almeida.
    '''
    if nome == '' and tot == '':
        t = 0
        n = '<desconhecido>'
        print(f'O jogador {n} fez {t} gol(s) no campeonato')
    elif nome == '':
        n = '<desconhecido>'
        print(f'O Jogador {n}, fez {t} gol(s) no campeonato')
    elif tot == '':
        t = 0
        print(f'O Jogador {n}, fez {t} gol(s) no campeonato')
    else:
        print(f'O Jogador {n}, fez {t} gol(s) no campeonato')


print(f'{"Ficha do jogador":^41}')
nome = str(input('Nome do jogador: '))
tot = str(input('Total de gols: '))
if tot.isnumeric():
    tot = int(tot)
else:
    tot = 0
ficha(nome, tot)
