'''
    DESAFIO 042

Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    - Equilátero: Todos os lados iguais.
    - Isósceles: dois lados iguais.
    - Escaleno: Todos os lados diferentes.
'''

print('-' * 8, 'Tipos de triângulos', '-' * 8)

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if (r1 + r2 < r3) or (r1 + r3 < r2) or (r2 + r3 < r1):
    print('\033[31mNão\033[m é um triângulo.')
elif (r1 == r2) and (r1 == r3):
    print('É um triângulo \033[34mequilátero.\033[m')
elif (r1 == r2) or (r1 == r3) or (r2 == r3):
    print('É um triângulo \033[34misósceles.\033[m')
elif (r1 != r2) and (r1 != r3) and (r2 != r3):
    print('É um triângulo \033[34mescaleno.\033[m')
