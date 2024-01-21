'''
DESAFIO 060

Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''

print('{:^52}'.format('Fatorial'))
n = int(input('Digite um número:'))
result = 1
count = 1
while count <= n:
    result *= count
    count += 1
print('Fatorial de 5!= {}'.format(result))
