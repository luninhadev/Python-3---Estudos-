'''
DESAFIO 102

Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e o outro chamdo show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela
o processo de cálculo do fatorial.
'''
def fatorial(n, show = False):
    '''
    ->Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: [opcional] mostra ou não a conta
    :return: O valor do fatorial de um número n.
    Função criada por Luna de Almeida.
    '''
    f = 1
    if show == False:
        for c in range(n, 1, -1):
            f *= c
        print(f'Fatorial de {n} é: {f}')
    else:
        print(f'{n}', end='')
        for c in range(n, 1, -1):
            f *= c
            print(f' x {c - 1}', end='')
        print(f' = {f}')


print(f'{"Função Fatorial":^41}')
fatorial(5, True)
fatorial(5)
help(fatorial)
