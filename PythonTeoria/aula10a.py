'''
    IF E ELSE
'''

nome = str(input('Digite seu nome: ')).strip().title()
if nome == 'Luna':
    print('Que nome lindo você tem {}'.format(nome))
else:
    print('Seu nome é tão comum!')
    print('Bom dia {}!'.format(nome))

'''
Exemplo de condição simplificada:
m sendo a média do aluno
print('PARABENS!' if m >= 6 else 'ESTUDE MAIS!')
'''