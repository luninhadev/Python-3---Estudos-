'''
DESAFIO 101

Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal, indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''
def voto(string):
    from datetime import datetime
    idade = datetime.now().year - string
    if idade < 16:
        print(f'Com {idade} anos: voto NEGADO')
    elif (idade >= 16) and (idade <= 17):
        print(f'Com {idade} anos: voto OPCIONAL')
    elif (idade >= 18) and (idade < 65):
        print(f'Com {idade} anos: voto OBRIGATÓRIO')
    else:
        print(f'Com {idade} anos: voto OPCIONAL')


print(f'{"Voto":^41}')
nasc = int(input('Digite o ano de nascimento: '))
voto(nasc)
