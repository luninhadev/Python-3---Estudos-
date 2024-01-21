for c in range(1, 6):
    print(c)
print('FIM')
for c in range(6, 1, -1):
    print(c)
print('FIM')
#Pulando de 2 em 2

for c in range(1, 6, 2):
    print(c)
print('FIM')
n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('FIM')

#Pulando de passo em passo
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('FIM')
