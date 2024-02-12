def metade(v=0, sit=False):
    '''
    ->Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param v: valor que se quer reajustar
    :param a: porcentagem do aumento
    :param r: porcentagem da redução
    :return: o valor reajustado com ou sem formatação
    '''
    resp = v / 2
    moeda = 'R$'
    if sit:
        return f'{moeda}{resp:.2f}'.replace('.', ',')
    else:
        return resp


def dobro(v=0, sit=False):
    resp = v * 2
    moeda = 'R$'
    if sit:
        return f'{moeda}{resp:.2f}'.replace('.', ',')
    else:
        return resp


def aumentar(v=0, taxa=0, sit=False):
    resp = v + (v * taxa/100)
    moeda = 'R$'
    if sit:
        return f'{moeda}{resp:.2f}'.replace('.', ',')
    else:
        return resp


def diminuir(v=0, taxa=0, sit=False):
    resp = v - (v * taxa/100)
    moeda = 'R$'
    if sit:
        return f'{moeda}{resp:.2f}'.replace('.', ',')
    else:
        return resp


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(p=0, a=0, r=0):
    print(f'\033[34;30;43m{"-" * 41:^41}\033[m')
    print(f'\033[34;30;43m{"RESUMO DO VALOR":^41}\033[m')
    print(f'\033[34;30;43m{"-" * 41:^41}\033[m')
    print(f'\033[34;30;43m{f" O preço analisado: {moeda(p):>20} ":<20}\033[m ')
    print(f'\033[34;30;43m{f" Metade do preço: {metade(p, True):>22}":<41}\033[m')
    print(f'\033[34;30;43m{f" Dobro do preço: {dobro(p, True):>23}":<41}\033[m')
    print(f'\033[34;30;43m{f" {a}% de aumento: {aumentar(p, a, True):>23}":<41}\033[m')
    print(f'\033[34;30;43m{f" {r}% de redução: {diminuir(p, r, True):>23}":<41}\033[m')
    print(f'\033[34;30;43m{"-" * 41:^41}\033[m')
