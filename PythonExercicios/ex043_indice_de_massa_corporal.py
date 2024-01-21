'''
DESAFIO 043

Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo:
    - Abaixo de 18.5: Abaixo do peso.
    - Entre 18.5 e 25: Peso ideal.
    - 25 até 30: Sobrepeso.
    - 30 até 40: Obesidade.
    - Acima de 40: Obesidade mórbida.
'''

print('-' * 8, 'Cálculo de IMC', '-' * 8)

kg = float(input('Digite seu peso em kg: '))
alt = float(input('Digite sua altura em metros: '))

imc = float(kg / (alt ** 2))

if imc <= 18.5:
    print('IMC: {:.1f}\nAbaixo do peso.'.format(imc))
elif (imc > 18.5) and (imc < 25):
    print('IMC: {:.1f}\nPeso ideal.'.format(imc))
elif (imc >= 25) and (imc < 30):
    print('IMC: {:.1f}\nSobrepeso.'.format(imc))
elif (imc > 30 ) and (imc <= 40):
    print('IMC: {:.1f}\nObesidade.'.format(imc))
elif imc > 40:
    print('IMC: {:.1f}\nObesidade mórbida.'.format(imc))
