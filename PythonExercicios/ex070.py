'''
DESAFIO 070

Crie um programa que leia nome e o preço de varios produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
    - A) Qual é o total gasto na compra
    - B) Quantos produtos custam mais de R$1.000,00
    - C) Qual é o nome do produto mais barato
'''
print(f'{"COMPRAS":^45}')
maismil = 0
nomeprod = str(input('Nome do produto: '))
precoprod = float(input('Preço: R$'))
continuar = str(input('Quer continuar? [S/N]: ')).upper()
menor = precoprod
total = precoprod
barato = nomeprod
while True:
    nomeprod = str(input('Nome do produto: '))
    precoprod = float(input('Preço: R$'))
    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    total += precoprod
    if precoprod <= menor:
        menor = menor
        barato = nomeprod
    if precoprod >= 1000:
        maismil += 1
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N]: ')).upper()
    if continuar == 'N':
        print(f'{"FIM DAS COMPRAS":^45}')
        print(f'{"":_^45}')
        print(f'Total gasto {total:.2f}\n{maismil} produtos custam mais de R$1.000,00\nO produto mais barato é {barato}')
        break
