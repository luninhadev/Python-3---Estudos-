'''
DESAFIO 071

Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui céddulas de R$50,00; R$20,00; R$10,00; e R$1,00.
'''
print(f'{"=" * 45}')
print(f'{"BANCO CEV":^45}')
print(f'{"=" * 45}')
n = int(input('Qual valor você quer sacar: R$'))
cedula = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
while True:
    if cedula < n and cedula < (n - 49):
        cedula += 50
        nota50 += 1
    elif cedula < n and cedula < (n - 19):
        cedula += 20
        nota20 += 1
    elif cedula < n and cedula < (n - 9):
        cedula += 10
        nota10 += 1
    elif cedula < n and cedula <= n:
        cedula += 1
        nota1 += 1
    elif cedula == n:
        print(f'{nota50} notas de R$50,00')
        print(f'{nota20} notas de R$20,00')
        print(f'{nota10} notas de R$10,00')
        print(f'{nota1} notas de R$1,00')
        break
