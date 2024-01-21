# DESAFIO 018

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians,sin,cos,tan

print('-' * 8, 'Seno Cosseno e Tangente', '-' * 8)

ang = int(input('Digite o valor de um ângulo: '))

# converte o ângulo em radiano:
rad = radians(ang)

seno = sin(rad)
cosseno = cos(rad)
tang = tan(rad)

print('Os valores são\nPara seno: {:.3f}\nPara cosseno: {:.3f}\nPara tangente: {:.3f}'.format(seno,cosseno,tang))
