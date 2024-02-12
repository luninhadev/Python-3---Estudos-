def metade(v=0, sit=False):
    resp = v / 2
    return resp if sit is False else moeda(resp)


def dobro(v=0, sit=False):
    resp = v * 2
    return resp if sit is False else moeda(resp)


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
