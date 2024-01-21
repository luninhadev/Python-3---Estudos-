# DESAFIO 15

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

km = int(input('Quantos quilometros o carro andou: '))
dia = int(input('O carro foi alugado por quantos dias: '))
vdia = dia * 60
vkm = km * 0.15

print('O valor a ser pago é R${:.2f}'.format(vdia + vkm))
