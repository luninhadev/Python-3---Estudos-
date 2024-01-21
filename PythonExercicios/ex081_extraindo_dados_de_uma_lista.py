'''
DESAFIO 081

Crie um programa que vai ler vários números e colocar numa lista. Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores de valores ordenados de forma decrescente.
    C) Se o valor 5 foi digitado e se está ou não na lista.
'''
lista = []
print('Desafio 081')
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    if continuar != 'S':
        print(f'Os valores digitados foram {lista}')
        print(f'Foram Digitados: {len(lista)} números')
        lista.sort(reverse=True)
        print(f'Lista em ordem decrescente: {lista}')
        if 5 in lista:
            print('O número 5 está na lista.')
        else:
            print('O número 5 não está na lista.')
        break
