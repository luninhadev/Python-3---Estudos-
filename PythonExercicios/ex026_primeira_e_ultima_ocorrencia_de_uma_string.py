'''
DESAFIO 026

Faça um programa que leia uma frase pelo teclado e mostre:
    - Quantas vezes aparece a letra "A"
    - Em que posição ela aparece a primeira vez
    - Em que posição ela aparece a última vez.
'''

print('-' * 8, 'Manipulando frases', '-' * 8)
frase = input('Digite uma frase: ').strip().upper()

quant = frase.count('A')
prim = frase.find('A')
ult = frase.rfind('A')
frase = frase.title()

print('A frase digitada: {}\nQuantidade de vezes que aparece a letra "A": {}\nEla aparece a primeira vez na posição: {}\nEla aparece a última vez na posição: {}'.format(frase, quant, prim + 1, ult + 1))
