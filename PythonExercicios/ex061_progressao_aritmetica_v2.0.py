'''
DESAFIO 061

Refaça o desafio 051, lendo o primeiro termo e a razão de uma P.A. mostrando os 10 primeiros termos da progressão
usando a estrutura while.
'''

print('{:=^52}'.format('Progressão Aritmética'))

termo1 = int(input('Digite o 1° termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
result = termo1 - razao
print('Os 10 termos dessa P.A. são:')
count = 0
while count < 10:
    result += razao
    count += 1
    print('[{}]'.format(result), end=' ')
'''
for c in range(termo1, decimo + razao, razao):
    print('[{}]'.format(c), end=' ')
'''