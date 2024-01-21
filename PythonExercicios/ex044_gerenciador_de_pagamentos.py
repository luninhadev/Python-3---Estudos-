'''
DESAFIO 044

Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:
    - À vista dinheiro/ cheque: 10% de desconto.
    - À vista no cartão: 5% de desconto.
    - Em até 2x no cartão: preço normal.
    - 3x ou mais no cartão: 20% de juros.
'''

print('-' * 8, 'Vendas', '-' * 8)

v = float(input('Digite o valor do produto: R$'))
print('Condições de pagamento:\n1 - À vista em dinheiro (10% desc).\n2 - À vista no cartão (5% desc)\n3 - Até 2x no cartão.\n4 - 3x ou mais no cartão (20% juros)')
cp = int(input('Digite a condição de pagamento: '))

if cp == 1:
    vd = v * 0.10
    vpd = v - vd
    print('Valor do produto: R${:.2f}\nValor de desconto: R${:.2f}\nValor do produto com o desconto: R${:.2f}'.format(v, vd, vpd))
elif cp == 2:
    vd = v * 0.05
    vpd = v - vd
    print('Valor do produto: R${:.2f}\nValor de desconto: R${:.2f}\nValor do produto com o desconto: R${:.2f}'.format(v, vd, vpd))
elif cp == 3:
    vd = 0
    vpd = v - vd
    print('Valor do produto: R${:.2f}\nValor de desconto: R${:.2f}\nValor do produto com o desconto: R${:.2f}'.format(v, vd, vpd))
elif cp == 4:
    vj = v * 0.20
    vpd = v + vj
    print('Valor do produto: R${:.2f}\nValor do juros: R${:.2f}\nValor do produto com o juros: R${:.2f}'.format(v, vj, vpd))
