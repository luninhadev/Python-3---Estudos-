'''DESAFIO 112

Dentro do pacote utilidadeCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função input mas com uma validação de dados para aceitarapenas
valores que sejam monetários.
'''
from ex111.utilidadesCeV import moeda
from ex111.utilidadesCeV.dado import leiaDinheiro
print(f'\033[34;30;43m{"-" * 41:^41}\033[m')
print(f'\033[34;30;43m{"Exercitando modulos em pyhton":^41}\033[m')
print(f'\033[34;30;43m{"-" * 41:^41}\033[m')
preco = leiaDinheiro('Digite o preço: R$')
moeda.resumo(preco, 20, 12)
