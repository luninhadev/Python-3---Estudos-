'''
DESAFIO 064

Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles.
'''

print('{:^45}'.format('Números, digitos e soma. Máximo de 999'))
start = 1
count = 0
soma = 0
while start != 0:
    n = int(input('Digite um número: '))
    if n == 999:
        start = 0
    else:
        count += 1
        soma += n
        print('Números digitados: {}\nSoma entres eles: {}'.format(count, soma))
        print('\n')
