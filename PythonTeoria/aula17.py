num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 0)
num.pop() # Exclui o elemento no último indice
num.pop(2) # Exclui o elemento do indice 2
num.remove(2) # percorre toda lista da esquerda pra direita procurando o primeiro elemento de valor 2
if 5 in num:
    num.remove(5)
else:
    print('Número 5 não encontrado')
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = [5, 9, 4]
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a # Faz uma ligação com a lista a
b = a[:] # faz uma cópia separada de a
b[2] = 8
print(f'{a}\n{b}')
