# DESAFIO 004

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

n = input('Digite algo: ')

print(n, 'é numérico: ', n.isnumeric())
print(n, 'é alfanumérico: ', n.isalnum())
print(n, 'é alfa: ', n.isalpha())
print(n, 'é ASCII: ', n.isascii())
print(n, 'é dígito: ', n.isdigit())
print(n, 'é decimal: ', n.isdecimal())
print(n, 'é identificador: ', n.isidentifier())
print(n, 'é minúscula: ', n.islower())
print(n, 'é maiúscula: ', n.isupper())
print(n, 'é impressa: ', n.isprintable())
print(n, 'é espaço em branco: ', n.isspace())
print(n, 'é título: ', n.istitle())
print(n, 'é uma subclasse: ', n.__init_subclass__())
