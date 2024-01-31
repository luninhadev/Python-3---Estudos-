def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


def contador(*num):
    s = 0
    for valor in num:
        s += valor
    print(f'Somando os valores {num} temos {s}')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


#Programa Principal
soma(4, 5)
soma(b=8, a=9)
soma(a=2, b=1)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
