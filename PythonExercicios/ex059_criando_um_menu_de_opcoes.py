'''
DESAFIO 059

Crie um programa que leia dois valores e mostre um menu na tela:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

print('{:^52}'.format('Operações'))
ns = [0, 0]
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
ns[0] = n1
ns[1] = n2
start = 1
while start == 1:
    print('[ 1 ] Somar.\n[ 2 ] Multiplicar.\n[ 3 ] Maior.\n[ 4 ] Novos números.\n[ 5 ] Sair do programa.')
    menu = int(input('Digite: '))
    if menu == 1:
        result = 0
        for c in range(0, len(ns)):
            result += ns[c]
        print('\033[34mNúmeros digitados: {}\033[m'.format(ns))
        print('\033[34mA soma é {}\033[m'.format(result))
    elif menu == 2:
        result = ns[0]
        for c in range(1, len(ns)):
            result *= ns[c]
        print('\033[34mNúmeros digitados: {}\033[m'.format(ns))
        print('\033[34mA multiplicação é: {}\033[m'.format(result))
    elif menu == 3:
        for c in range(0, len(ns)):
            result = ns[0]
            while result < ns[c]:
                result = ns[c]
                print('\033[34mNúmeros digitados: {}\033[m'.format(ns))
                print('\033[34mMaior número: {}\033[m'.format(result))
    elif menu == 4:
        n3 = int(input('Digite um novo número: '))
        ns.append(n3)
    elif menu == 5:
        start = -1
    else:
        print('\033[31mDigite um número entre 1 e 5\033[m')
