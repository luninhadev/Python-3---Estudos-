'''
n = 1
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    s += n
print(f'A soma é: {s}')
'''

nome = 'José'
idade = 33
salario = 1322.97
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')
print(f'O {nome:20} tem {idade} anos e ganha R${salario:.2f}')
print(f'O {nome:^20} tem {idade} anos e ganha R${salario:.2f}')
print(f'O {nome:>20} tem {idade} anos e ganha R${salario:.2f}')
print(f'O {nome:-<20} tem {idade} anos e ganha R${salario:.2f}')
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}')
print(f'O {nome:->20} tem {idade} anos e ganha R${salario:.2f}')
print(f"{f'O {nome} tem {idade} anos e ganha R${salario:.2f}':^45}")
