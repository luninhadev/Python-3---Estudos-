'''
DESAFIO 092

Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e
o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import date
trabalhador = {'nome': '',
               'idade': 0,
               'carteira de trabalho': {'ano contratacao': 0,
                                        'salario': 0.0}}
print(f'{"Cadastro de Trabalhador":^41}')
nome = str(input('Digite seu nome: '))
nascimento = int(input('Digite seu ano de nascimento: '))
carteira = str(input('Tem carteira de trabalho [S/N]: ')).upper()
if carteira in 'S':
    trabalhador['carteira de trabalho']['ano contratacao'] = int(input('Digite o ano de contratação: '))
    trabalhador['carteira de trabalho']['salario'] = float(input('Digite o salario: '))
trabalhador['nome'] = nome
trabalhador['idade'] = date.today().year - nascimento
print(f'{"Trabalhador Cadastrado":-^41}')
print(f'Nome: {trabalhador["nome"]}')
print(f'Idade: {trabalhador["idade"]}')
print(f'CTPS : {carteira}')
print(f'Ano de contratação: {trabalhador["carteira de trabalho"]["ano contratacao"]}')
print(f'Salário: R${trabalhador["carteira de trabalho"]["salario"]}')
if carteira in 'S':
    aposentadoria = 35 - (date.today().year - trabalhador['carteira de trabalho']['ano contratacao'])
    print(f'Tempo para aposentar: {aposentadoria} ano(s)')
