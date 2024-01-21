'''
DESAFIO 063

Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência
de Fibonacci.
'''

print('{:^52}'.format('Sequência de Fibonacci'))
start = 1
while start != 0:
    n = int(input(('Quantos elementos da sequência de Fibonacci?: ')))
    fn = [0, 1]
    i = 0
    while len(fn) < n:
        fn.append(fn[i] + fn[i+1])
        i += 1
    if n > 0:
        print('\n\033[34mOs elementos da sequência de Fibonacci são:\033[m')
        for c in range(0, len(fn)):
            print('\033[33m-->\033[m {}'.format(fn[c]), end=' ')
        print('\n')
    elif n == 0:
        start = 0
