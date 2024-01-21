'''
DESAFIO 048

Faça um programa que calcule a soma entre todos os número ímpares que são múltiplos de três e que se encontram de 1
até 500.
'''

print('{:^52}'.format('Cálculo da soma dos números impares múltiplos de três'))
soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 2 != 0:
        if c % 3 == 0:
            cont += 1
            soma += c
print('A soma: {}'.format(soma))
print('Quantidade somada: {}'.format(cont))
