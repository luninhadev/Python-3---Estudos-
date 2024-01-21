# DESAFIO 12

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o preço do produto : '))
desc = p-(p*0.05)

print('Preço do produto é R${}\nCom desconto de 5%: R${:.2f}'.format(p,desc))
