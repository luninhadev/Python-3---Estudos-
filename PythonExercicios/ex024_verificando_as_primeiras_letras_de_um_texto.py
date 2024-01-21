'''
DESAFIO 024

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.
'''

print('-' * 8, 'Verificar se cidade começa com "Santo"', '-' * 8)

cidad = str(input('Digite o nome de uma cidade: ')).strip()
cidade = cidad.split()
cidade[0] = cidade[0].capitalize()
cidade = bool('Santo' in cidade[0])

# print(cidad[:5].capitalize() == 'Santo')

if (cidade == True):
    print('A cidade digitada começa com "Santo"!')
else:
    print('A cidade digitada não começa com "Santo"')
