'''DESAFIO 110

Adcione ao modulo da moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
informações geradas pelas funções que já temos no módulo criado até aqui.
'''
from ex110 import moeda
print(f'{"Exercitando modulos em pyhton":^41}')
preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 20, 12)
