'''
DESAFIO 085

Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
valores = list()
pares = list()
impares = list()
print(f'{"7 valores, pares e ímpares":^41}')
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}° valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
valores.append(pares[:])
valores.append(impares[:])
print(valores)
print('Em ordem crescente:')
pares.sort()
impares.sort()
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados são: {valores[0]}')
print(f'E os valores ímpares digitados são: {valores[1]}')
