'''
DESAFIO 025

Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
'''

print('-' * 8, 'Tem "Silva" no seu nome?', '-' * 8)

nome = input('Digite o seu nome: ').strip().title()
verif = bool('Silva' in nome)

if (verif == True):
    print('Sim! Você tem "Silva" no seu nome')
else:
    print('Não... Infelizmente não encontramos "Silva" no seu nome.')
