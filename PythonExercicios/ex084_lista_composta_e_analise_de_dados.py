'''
DESAFIO 084

Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
no final mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas
    C) Uma listagem com as pessoas mais leves
'''
print(f'{"Pesos":^41}')
pessoas = list()
info = list()
qtd = 0
pesadas = 0
leves = 0
while True:
    info.append(str(input('Digite o nome: ')))
    info.append(float(input('Digite o peso: ')))
    pessoas.append(info[:])
    if info[1] >= 100:
        pesadas += 1
    if info[1] <= 99:
        leves += 1
    info.clear()
    qtd += 1
    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    if continuar != 'S':
        print(pessoas)
        print(f'{qtd} pessoas foram cadastradas')
        print(f'Tem {pesadas:.0f} pessoas pesadas, acima de 100kg')
        print(f'Tem {leves:.0f} pessoas leves, abaixo de 100kg')
        break
