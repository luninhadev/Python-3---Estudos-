'''
Desafio 082

Crie um programa que vai ler vários números e colocar em uma lista. Depois disso crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares. respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
listapares = []
listaimpares = []
print(f'{"Desafio 082":^41}')
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    if continuar != 'S':
        print(f'{"":-^41}')
        print(f'Os valores digitados foram: {lista}')
        for c in range(0, len(lista)):
            if lista[c] % 2 == 0:
                listapares.append(lista[c])
            if lista[c] % 2 != 0:
                listaimpares.append(lista[c])
        print(f'Lista com números pares: {listapares}')
        print(f'Lista com números ímpares: {listaimpares}')
        break
