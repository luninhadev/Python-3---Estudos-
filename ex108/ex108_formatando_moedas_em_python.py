'''
DESAFIO 107

Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade()
Faça também um programa que importe esse módulo e use alguma dessas funções
'''
from ex108 import moeda
print(f'{"Exercitando modulos em pyhton":^41}')
preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é : {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é : {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 10% temos: {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'Diminuindo 13% temos: {moeda.moeda(moeda.diminuir(preco, 13))}')
