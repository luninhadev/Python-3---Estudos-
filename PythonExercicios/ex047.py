'''
DESAFIO 047

Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50.
'''

print('{:=^45}'.format('Números Pares de 1 a 50'))

for c in range(1, 51):
    if (c % 2) == 0:
        print(c)

'''
Mais eficiente

print('{:=^45}'.format('Números Pares de 1 a 50'))

for c in range(2, 51, 2):
        print(c)
'''