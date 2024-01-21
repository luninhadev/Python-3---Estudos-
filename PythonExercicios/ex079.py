'''
DESAFIO 079

Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o
número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores unicos digitados em ordem
crescente.
'''
valores = []
print(f'{"Valores sem repetição":^41}')
continuar = 's'
while continuar in 'Ss':
    n = (int(input('Digite um valor: ')),)
    if n in valores:
        print('Número já existe... não foi adcionado')
    else:
        valores.append(n)
        print('Adiicionado com sucesso!')
    continuar = str(input('Quer continuar? [s/n]: '))
    if continuar in 'Nn':
        print(sorted(valores))
        print('FIM')
        break
