'''
DESAFIO 077

Crie um programa que tenha uma tupla com várias palavras (nao usar acentos).Depois disso, você deve mostrar, para
cada palavra, quais são suas vogais.
'''
listagem = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
vogais = ('a', 'e', 'i', 'o', 'u')
print(f'{"":-^41}')
print(f'{"PALAVRAS E VOGAIS":^41}')
print(f'{"":-^41}')
for p in listagem:
    print(f'\nNa palavra [{p.upper()}] temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end='')
print(f'{"":-^41}')

