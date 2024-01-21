# DESAFIO 11

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

print('Quantos litros de tinta preciso para pintar minha parede?')

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
area = l*a
tinta = area/2

print('Sua parede tem uma área de {:.3f}m², será necessário {:.3f} litros de tinta para pintá-la'.format(area,tinta))