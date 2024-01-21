'''
DESAFIO 033

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

print('-' * 8, 'Maior e menor número', '-' * 8)
def maior(n1, n2, n3):
    max = n1

    if n2 > max:
        max = n2
    if n3 > max:
        max = n3

    return max


def menor(n1, n2, n3):
    min = n1

    if n2 < min:
        min = n2
    if n3 < min:
        min = n3

    return min


n = int(input('Digite três números: '))
nstr = str(n)
n1 = nstr[0]
n2 = nstr[1]
n3 = nstr[2]

print('O maior valor digitado é {}'.format(maior(n1, n2, n3)))
print('O menor valor digitado é {}'.format(menor(n1, n2, n3)))

'''RESOLUÇÃO SEM CRIAR FUNÇÃO---------------------------------------------------------------------------------------

print('-' * 8, 'maior e menor', '-' * 8)

n = int(input('Digite três números: '))

nstr = str(n)
n1 = nstr[0]
n2 = nstr[1]
n3 = nstr[2]
maior = nstr[0]
menor = nstr[0]

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print('Maior é {}\nMenor é {}'.format(maior, menor))

'''