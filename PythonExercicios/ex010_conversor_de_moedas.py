# DESAFIO 10

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

print('Converter reais para dolares a um câmbio de 5,01')

n = int(input('Quanto você tem na sua carteira: '))
rc = n/5.01

print('Você pode comprar US${:.2f} com R${}'.format(rc,n))