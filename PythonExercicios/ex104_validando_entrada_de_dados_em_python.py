'''
DESAFIO 104

Crie um programa que tenha a função leiaInt() que vai funcionar de forma semelhante à função input() do python, só
que fazendo a validação para aceitar apenas um valor númérico.

Ex:
n = leiaInt('Digite um número: ')
'''
def leiaInt(msg):
    '''
    ->Vai receber o valor da msg verificar se é número e retornar o resultado ou pedir um número válido
    :param msg: valor do input do programa principal
    Função feita por Luna Almeida.
    '''
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


print(f'{"Validando entrada de dados em Python":^41}')
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
