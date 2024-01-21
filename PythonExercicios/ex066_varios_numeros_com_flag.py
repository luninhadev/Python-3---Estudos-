'''
DESAFIO 066

Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar o valor
999 é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles.
'''

print('Números e a soma entre eles')
n = count = s = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    s += n
    count += 1
print(f'\nForam digitados {count} números\nA soma entre os números foi: {s}')
