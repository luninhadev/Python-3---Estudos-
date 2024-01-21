'''
DESAFIO 057

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado peça a digitação novamente até ter uma valor correto.
'''

print('{:^52}'.format('"M" ou "F"'))

sexo = str(input('Digite seu sexo: '))

while sexo not in 'M' and sexo not in 'm' and sexo not in 'F' and sexo not in 'f':
    sexo = str(input('Digite seu sexo [M/F]: '))
