'''
DESAFIO 086

Crie um programa que crie uma matriz de dimensão 3x3 e preenchea com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''
matriz = list()
print(f'{"Matriz":^41}')
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para {l, c}: '))
        matriz.append(n)
for c in range(0, 9, 3):
    print(f' [ {matriz[c]:^5} ] ', end='')
    print(f' [ {matriz[c + 1]:^5} ] ', end='')
    print(f' [ {matriz[c + 2]:^5} ] ')
