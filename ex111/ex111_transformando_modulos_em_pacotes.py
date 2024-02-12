'''DESAFIO 111

Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo
funcionando.
'''
from ex111.utilidadesCeV import dado, moeda
print(f'\033[34;30;43m{"-" * 41:^41}\033[m')
print(f'\033[34;30;43m{"Exercitando modulos em pyhton":^41}\033[m')
print(f'\033[34;30;43m{"-" * 41:^41}\033[m')
preco = float(input(f'Digite o preço: R$'))
moeda.resumo(preco, 20, 12)
