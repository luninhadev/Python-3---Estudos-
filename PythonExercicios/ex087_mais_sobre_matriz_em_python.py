'''
DESAFIO 087

Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.
'''
matriz = list()
pares = 0
coluna3 = 0
maior = 0
print(f'{"Matriz Aprimorada":^41}')
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para {l, c}: '))
        matriz.append(n)
        if n % 2 == 0:
            pares += n
for c in range(0, 9, 3):
    print(f' [ {matriz[c]} ] ', end='')
    print(f' [ {matriz[c + 1]} ] ', end='')
    print(f' [ {matriz[c + 2]} ] ')
    coluna3 += matriz[c + 2]
for c in range(3, 6):
    maior = matriz[c]
    if matriz[c] >= maior:
        maior = matriz[c]
print(f'A soma de todos os valores pares é: {pares}')
print(f'A soma da terceira coluna é: {coluna3}')
print(f'O maior número da segunda linha é {maior}')
