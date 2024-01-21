'''
DESAFIO 050

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for impar desconsidere-o.
'''

print('{:^52}'.format('Soma dos pares'))

soma = 0
listnum = [0, 0, 0, 0, 0, 0]
pares = [0, 0, 0, 0, 0, 0]
for c in range(0, 6):
    listnum[c] = int(input('Digite um número inteiro: '))

for c in range(0, 6):
    if (listnum[c] % 2) == 0:
        soma += listnum[c]
        pares[c] = listnum[c]
print('{:^52}'.format('A soma dos números pares é: {}'.format(soma)))
print('{:^52}'.format('Números pares digitados: {}'.format(pares)))
