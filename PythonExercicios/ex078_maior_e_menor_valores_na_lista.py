'''
DESAFIO 078

Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final mostre qual foi o menor e o maior valor e as suas respectivas posições na lista
'''
valores = []
print(f'{"Maior e Menor"}')
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c+1}° valor: ')))
maiores = max(valores)
print(f'Valores digitados {valores}')
for pos, v in enumerate(valores):
    if max(valores) == valores[pos]:
        print(f'O maior valor: {max(valores)} está na {pos + 1}° posição',)
    if min(valores) == valores[pos]:
        print(f'O menor valor: {min(valores)} está na {pos + 1}° posição')
