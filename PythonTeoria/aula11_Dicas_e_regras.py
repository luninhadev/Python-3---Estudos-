'''
    COLOCANDO CORES NO PYTHON
'''

print('\033[1;33;44mOlá, Mundo\033[m')
print('\033[7;30;45mOlá, Mundo\033[m')

a = 3
b = 5

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = str('Luna')

print('Olá! Muito prazer em te conhecer {}{}{}!!'.format('\033[4;32m', nome, '\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto e branco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))
