'''DESAFIO 109

Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pelo função moeda(), desenvolvida no desafio 108
'''
from ex109 import moeda
print(f'{"Exercitando modulos em pyhton":^41}')
preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é: {moeda.metade(preco, False)}')
print(f'O dobro de {moeda.moeda(preco)} é: {moeda.dobro(preco, True)}')
print(f'Aumentando 10% temos: {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo 13% temos: {moeda.diminuir(preco, 13, True)}')