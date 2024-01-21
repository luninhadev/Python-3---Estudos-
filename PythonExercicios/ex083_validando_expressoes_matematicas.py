'''
DESAFIO 083

Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
a expressão passada está com os parênteses abertos e fechados na ordem correta. e mostras se está correta ou errada
'''

print(f'{"Validador de expressões":^41}')
expressao = str(input('Digite uma expressão usando parênteses: '))
aberto = 0
fechado = 0
if '(' in expressao:
    for c in range(len(expressao)):
        if '(' in expressao[c]:
            aberto += 1
        if ')' in expressao[c]:
            fechado += 1
    print(f'Exitem {aberto} parênteses abertos nesta expressão.')
    print(f'Exitem {fechado} parênteses fechados nesta expressão.')
    if aberto == fechado:
        print(f'A expressão {expressao} está correta.')
    else:
        print(f'A expresão {expressao} está errada.')
else:
    print('Você esqueceu dos parênteses')
