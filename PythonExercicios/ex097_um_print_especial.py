'''
DESAFIO 097

Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
uma mensagem com tamanho adaptável
Ex:
escreva('Olá, Mundo!')
'''
def escreva(txt):
    tam = len(txt) + 2
    print(f'~' * tam)
    print(f' {txt}')
    print(f'~' * tam)


print(f'{"Um print especial":^41}')
msg = str(input('Digite uma frase: '))
escreva(msg)
