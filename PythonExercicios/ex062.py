'''
DESAFIO 062

Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 Termos.
'''

print('{:=^52}'.format('Progressão Aritmética'))

termo1 = int(input('Digite o 1° termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
result = termo1 - razao
ntermos = 1
count = 0
while ntermos != 0:
    ntermos = int(input('Quer mostrar quantos termos?: '))
    while count < ntermos:
        result += razao
        count += 1
        print('[{}]'.format(result), end=' ')
    print('\n')
    count = 0

