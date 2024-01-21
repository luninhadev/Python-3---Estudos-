'''
DESAFIO 075

Desenvolva um programa que leia quatro valores e guarde-os numa Tupla. No final mostre:
    - A) Quantas vezes apareceu o valor 9.
    - B) Em que posição foi digitado o primeiro valor 3.
    - C) Quais foram os números pares.
'''

print(f'{"4 Valores":^41}')
ntuplas = ()
cont = 0
primeirotres = 0
pares = ()
for c in range(0, 4):
    n = int(input(f'Digite o {c + 1}° valor: '))
    ntuplas += (n,)
for c in range(0, 4):
    if ntuplas[c] % 2 == 0:
        pares += (ntuplas[c],)
    if ntuplas[c] == 9:
        cont += 1
    if ntuplas[c] == 3:
        primeirotres = ntuplas[c]
print(f'Você digitou os valores: {ntuplas}')
if cont >= 1:
    print(f'O 9 apareceu {cont} vezes')
else:
    print('Nenhum 9 foi digitado')
if 3 in ntuplas:
    print(f'O 1° valor de 3 está na {primeirotres+1}° posição')
if 3 not in ntuplas:
    print('Não foi encontrado o valor 3')
print(f'Números pares digitados: {pares}')
