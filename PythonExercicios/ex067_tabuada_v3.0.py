'''
DESAFIO 067

Faça um programa que mostra a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''

print(f'{"Mostre a tabuada":^45}')
while True:
    n = int(input('De qual número deseja ver?: '))
    if n < 0:
        break
    print(f'{"":-^45}')
    for c in range(0, 11):
        print(f'{n} x {c} = {n*c}')
    print(f'{"":-^45}')
