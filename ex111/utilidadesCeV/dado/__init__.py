def leiaDinheiro(din):
    ok = False
    valor = 0
    while True:
        n = str(input(din))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO! Digite um valor monetário.\033[m')
        if ok:
            break
    return valor


