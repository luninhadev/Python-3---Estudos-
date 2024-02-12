def metade(v=0):
    return v / 2


def dobro(v=0):
    return v * 2


def aumentar(v=0, taxa=0):
    return v + (v * taxa/100)


def diminuir(v=0, taxa=0):
    return v - (v * taxa/100)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
