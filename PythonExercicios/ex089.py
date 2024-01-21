'''
DESAFIO 089

Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permit que o usuário possa mostrar as notas de cada aluno
individualmente.
'''
alunos = list()
dados = list()
notas = list()
print(f'{"Boletim Escolar":^41}')
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    media = (nota1 + nota2) / 2
    dados.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    dados.append(notas[:])
    dados.append(media)
    alunos.append(dados[:])
    dados.clear()
    notas.clear()
    if continuar in 'N':
        print(f'{"":-^41}')
        print(f'{"N°":<3}', f'{"NOME":<17}', f'{" MÉDIA":>18}')
        print(f'{"":-^41}')
        for i, a in enumerate(alunos):
            print(f'{i:<3}{a[0]:<18}{a[2]:>18.1f}')
        print(f'{"":-^41}')
        while True:
            aluno = int(input(('Mostrar media de qual aluno?: ')))
            for c in range(1):
                print(f'A notas de {alunos[aluno][c]} são: {alunos[aluno][1]}')
            sair = str(input('Deseja sair? [S/N]: ')).upper()
            print(f'{"":-^41}')
            if sair in 'S':
                break
        break
