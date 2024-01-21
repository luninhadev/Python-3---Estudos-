'''
    DESAFIO 037

    Escreva um programa que leia um número qualquer e peça para o usuário escolher qual será
a base de conversão.

    - 1 para binário
    - 2 para octal
    - 3 para hexadecimal
'''

print('-' * 8, 'Convertendo em bases numéricas', '-' * 8)
n = int(input('Digite um número: '))
b = int(input('''Em que base voce quer converter o {}?
[ 1 ] Binário.
[ 2 ] Octal.
[ 3 ] Hexadecimal.
Digite um número: '''.format(n)))

if b == 1:
    print('{} na base Binária é {}'.format(n, format(n, 'b')))
elif b == 2:
    print('{} na base Octal é {}'.format(n, format(n, 'o')))
elif b == 3:
    print('{} na base Hexadecimal é {}'.format(n, format(n, 'x')))
else:
    print('\033[31mDigite um número entre 1 e 3!\033[m')


'''NOTAS
    Em Python, pode utilizar uma função integrada, bin() para converter um número inteiro
em binário. A função bin() toma um inteiro como parâmetro e devolve a sua string binária
equivalente prefixada com 0b.

Um exemplo disto é:
binary = bin(16)
print(binary)

Resultado: 0b10000

    Como mostrado acima, o binário de um número inteiro pode ser simplesmente obtido com o
método bin(x). Mas se quiser remover o prefixo 0b da sua saída, pode utilizar a função format
e formatar a saída.

A função format(value, format_spec) tem dois parâmetros - value e format_spec. Retornará a
saída formatada de acordo com a função format_spec. Abaixo estão alguns exemplos de tipos de
formatação que podem ser utilizados dentro dos espaços reservados:

Tipo de formatação:
    =	Coloca o sinal na posição mais à esquerda
    b	Converte o valor em binário equivalente
    o	Converte o valor para o formato octal
    x	Converte o valor para o formato Hex
    d	Converte o valor dado em decimal
    E	Formato científico, com um E em maiúsculas
    X	Converte o valor para o formato Hex em maiúsculas

Exemplo:
temp = format(10, "b")
print(temp)

Resultado: 1010
'''