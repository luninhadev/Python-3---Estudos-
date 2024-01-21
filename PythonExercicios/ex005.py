# DESAFIO 05

# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('Digite um número inteiro: '))
su = n+1
an = n-1

print('O Antecessor de {} é {} e o sucessor é {}!'.format(n,an,su))