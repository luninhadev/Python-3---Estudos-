'''
DESAFIO 023

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separado.

Ex:
Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
'''

n = str(input('Digite um valor de 0 a 9999: '))

# contagem de zeros e atribuição de zeros pra totalizar 4 unidades ou 4 caracters
zero = int(4 - len(n))
n = ('0' * zero) + n

un = n[3]
de = n[2]
ce = n[1]
mi = n[0]

print('Número digitado: {}\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(n, un, de, ce, mi))

'''
TAMBÉM FUNCIONA!!
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
'''