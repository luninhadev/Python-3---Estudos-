'''
DESAFIO 029

Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada Km acima do limite.
'''

print('-' * 8, 'Limite de velocidade 80Km/h', '-' * 8)

vel = int(input('Digite a velocidade do carro: '))
multa = int()

if vel > 80:
    multa = (vel - 80) * 7
    print('Você passou {} do limite de velocidade!\nIrá receber uma multa de R${:.2f}'.format(vel - 80, multa))
else:
    print('Fique tranquilo(a) você está dentro do limite de velocidade.')
