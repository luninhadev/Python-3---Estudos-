# DEDAFIO 016

# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.

# Utilizar a função round() nesse caso é melhor porque ele arredonda tanto pra cima quanto pra baixo!

print('-'*5, 'Programa de arredondamento','-'*5)
n = float(input('Digite um número com duas casas decimais: '))

print('O arredondamento de {} é: {}'.format(n, round(n)))
