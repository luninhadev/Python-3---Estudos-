'''
DESAFIO 017

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e
mostre o comprimento da hipotenusa.
'''
from math import sqrt

print('-' * 8, 'TEOREMA DE PITÁGORAS', '-' * 8)
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjascente: '))
hip = sqrt((co ** 2) + (ca ** 2))
# hip = hypot(co, ca)

print('O comprimento da hipotenusa é: {:.2f}'.format(hip))
