'''
DESAFIO 096

Faça um programa que tenha uma função chamada area() que receba as dimensões de um terreno retangular (largura
e comprimento) e mostra a área do terreno
'''
def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m²')


print(f'{"Calcula área":^41}')
larg = float(input('Digite a largura do terreno: '))
comp = float(input('Digite o comprimento do terreno: '))
area(larg, comp)
