def leiaInt(msg):
    '''
    ->Vai receber o valor da msg verificar se é número e retornar o resultado ou pedir um número válido
    :param msg: valor do input do programa principal
    Função feita por Luna Almeida.
    '''
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def linha(tam=41):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(f'\033[34m{txt.center(41)}\033[m')
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
