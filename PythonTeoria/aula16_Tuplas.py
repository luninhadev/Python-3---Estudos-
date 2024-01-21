
tuplasemparenteses = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imutáveis
#lanche[1] = 'Refrigerante'
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2])
print(lanche[-3:])
print(sorted(lanche)) #Em ordem alfabética
#print(lanche[1]) <--- Erro: Tupla não aceita atribuição

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!!')


for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
    
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # concatena as Tuplas
print(c)
print(c.count(5)) # Quantas vezes aparece o número 5
print(c.index(8)) # retorna o index do 8
print(c.index(5, 2)) # retorna o 5 contando apartir do index 2, ou seja, apartir do 3° elemento

pessoa = ('Luna', 26, 'F', 58.5)
del(pessoa) # Apaga a Tupla
print(pessoa)
