# DESAFIO 08

# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('Conversor de metro em centímetro e milímetro')
m = int(input('Digite um valor em metro: '))
cm = m*100
mm = m*1000

print('Resultado\n{}m\n{}cm\n{}mm'.format(m,cm,mm))