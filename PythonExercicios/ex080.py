'''
DESAFIO 080

Crie um programa onde o usuário possa digitar cinco valores numericos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar sort()). No final, mostre a lista ordenada na tela.
'''
valores = []
continuar = 's'
print(f'{"Adicionando no meio da lista":^41}')
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicioando na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {valores}')
