# DESAFIO 13

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o valor do seu salário: '))
a = s+(s*0.15)

print('O salário é R${}\nCom aumento de 15% é R${:.2f}'.format(s,a))