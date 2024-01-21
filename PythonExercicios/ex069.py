'''
DESAFIO 069

Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final mostre:
    - A) Quantas pessoas tem mais de 18 anos
    - B) Quantos homens foram cadastrados
    - C) Quantas mulheres tem menos de 20 anos
'''
print(f'{"":-^45}')
print(f'{"CADASTRO":^45}')
print(f'{"":-^45}')
continuar = 'S'
maior18 = qtdhomens = mulhermenor20 = 0
while True:
    if (continuar == 'S') or (continuar != 'S'):
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [M/F]: ')).upper()
        while (sexo != 'M') and (sexo != 'F'):
            sexo = str(input('Sexo [M/F]: ')).upper()
        continuar = str(input('Quer continuar? [S/N]: ')).upper()
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('Quer continuar? [S/N]: ')).upper()
        if idade >= 18:
            maior18 += 1
        if sexo == 'M':
            qtdhomens += 1
        elif sexo == 'F' and idade <= 20:
            mulhermenor20 += 1
        if continuar == 'N':
            print(f'{"":-^45}')
            print(f'{"FIM DO PROGRAMA":^45}')
            print(f'{"":-^45}')
            print(f'Tem {maior18} maior de 18 anos.\nTem {qtdhomens} homens cadastrados.\nTem {mulhermenor20} mulheres menor de 20 anos')
            break
