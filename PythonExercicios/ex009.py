# DESAFIO 09

# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

print('TABUADA')
n = int(input('Digite um número inteiro: '))

for i in range(11):
    print('{} x {} = {}'.format(n,i,n*i))
