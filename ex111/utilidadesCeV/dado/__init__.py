def leiaDinheiro(din):
    valido = False
    valor = 0
    while True:
        n = str(input(din)).replace(',', '.').strip()
        if n.isalpha() or n.strip() == '':
            print(f'\033[0;31mERRO! \"{n}\" é um preço inválido.\033[m')
        else:
            valido = True
            return float(n)

