'''
DESAFIO 094

Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa num
dicionário e todos os dicionários numa lista. No final mostre:
    - A) Quantas pessoas foram cadastradas
    - B) A média de idade do grupo
    - C) Uma lista com todas as mulheres
    - D) Uma lista com todas as pessoas com idade acime da média
'''
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input(('Nome: ')))
    while True:
        pessoa['sexo'] = str(input(('Sexo [F/M]: '))).upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in "SN":
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 41)
print(f'A) A todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print(f'     ', end='')
        for k, v in p.items():
            print(f'{k}, = {v}, ', end='')
        print(f'')
print('<<ENCERRADO>>')
