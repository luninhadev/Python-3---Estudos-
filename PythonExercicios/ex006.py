# DESAFIO 06

# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e sua raiz quadrada.

n = int(input('Digite um número: '))
d = n*2
t = n*3
rq = n**(1/2)

print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.3f}.'.format(n,d,t,rq))
print(type(rq))