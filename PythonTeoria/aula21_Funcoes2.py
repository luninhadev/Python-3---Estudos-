def contador(i, f, p):
    '''
    --> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Luna de Almeida.
    '''
    c = i
    while c <= f:
        print(f'{c} ', end="")
        c += p
    print('FIM!')


def somar(a=0, b=0 , c=0):
    '''
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    Função criada por Luna de Almeida.
    '''
    s = a + b + c
    return s


def teste():
    x = 8
    print(f'Na função teste, n vale {n}')# A variável n tem escopo global (existe no código inteiro)
    print(f'Na função teste, x vale {x}')# A variável x tem escopo local (só existe dentro da função)


def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


#help(print())
#print(input.__doc__)

contador(2, 10, 2)

help(contador)

somar(4, 2)

n = 2
teste()

n1 = 2
funcao()
print(f'N1 fora vale {n1}')

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2}, {r3}')

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
