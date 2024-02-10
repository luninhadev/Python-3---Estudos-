'''
DESAFIO 105

Faça um programa que tenha uma função notas() que pode receber varias notas de alunos e vai retornar um dicionário
com as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)
Adcione também as docstrings da função
'''
def notas(*gnotas, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param gnotas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adcionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    Função feita por Luna de Almeida.
    '''
    notas = dict()
    notas['total'] = len(gnotas)
    notas['maior'] = max(gnotas)
    notas['menor'] = min(gnotas)
    notas['media'] = sum(gnotas) / len(gnotas)
    if sit:
        if notas['media'] > 7:
            notas['situação'] = 'BOA'
        elif notas['media'] >= 5:
            notas['situação'] = 'RAZOÁVEL'
        else:
            notas['situação'] = 'RUIM'
    return notas


print(f'{"Analisando e gerando dicionários":^41}')
resp = notas( 5.5, 2.5, sit=True)
print(resp)
help(notas)
