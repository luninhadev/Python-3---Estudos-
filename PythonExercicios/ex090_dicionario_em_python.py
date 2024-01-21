'''
DESAFIO 090

Faça um programa que leia nome e media de um aluno, guardando também a situação a situação em um dicionário. No final
mostre o conteúdo da estrutura na tela
'''
alunos = {'nome': '', 'media': 0, 'situacao': ''}
print(f'{"Situação aluno":^41}')
alunos['nome'] = str(input('Digite o nome do aluno: '))
alunos['media'] = float(input('Digite a media do aluno: '))
if alunos['media'] >= 7:
    print(f'O(a) aluno(a) {alunos["nome"]} está aprovado!')
else:
    print(f'O(a) aluno(a) {alunos["nome"]} está reprovado!')
