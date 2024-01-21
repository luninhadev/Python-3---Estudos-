'''
DESAFIO 056

Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final mostre:
    - A média da idade do grupo.
    - Qual nome do homem mais velho.
    - Quantas mulheres tem menos de 21 anos
'''

print('{:^52}'.format('Informações do grupo'))

nomes = ['', '', '', '']
idades = [0, 0, 0, 0]
sexo = ['', '', '', '']
somaidade = 0

print('Preencha o formulário a baixo')

# COLETA OS DADOS DO GRUPO E ATRIBUI A LISTA RESPECTIVA
for c in range(0, 4):
    nomes[c] = str(input('Nome da {}° pessoa do grupo: '.format(c+1))).strip()
    idades[c] = int(input('Sua idade: '))
    sexo[c] = str(input('Seu sexo (M) ou (F): ')).upper()
    print('{:_^60}'.format(''))
    somaidade += idades[c]  # SOMA A IDADE DE TODOS DO GRUPO

# VARIÁVEIS NO AUXILIO DOS CÁCULOS
medidade = somaidade / 4
maisvelho = ''
mulhermenos21 = 0

# LISTA ESPECÍFICA PARA HOMENS COM NOME E IDADE
homens = []
idadehomens = []

# ATRIBUI A CONTAGEM DAS MULHERES ABAIXO DOS 21 ANOS E CRIA UMA LISTA ESPECÍFICA PARA HOMENS
for c in range(0, 4):
    if (sexo[c] == 'F') and (idades[c] < 21):
        mulhermenos21 += 1
    elif sexo[c] == 'M':
            homens.append(nomes[c])
            idadehomens.append(idades[c])

idademaior = idadehomens[0]

# VERIFICA QUAL HOMEM É O MAIS VELHO
for c in range(0, len(homens)):
    if idadehomens[c] >= idademaior:
        maisvelho = homens[c]

print('{:^52}'.format('RESULTADO'))
print('A média da idade do grupo é {}.\nO homem mais velho é o {}.\nTem {} mulhere(s) abaixo dos 21 anos.'.format(medidade, maisvelho, mulhermenos21))

'''
RESOLUÇÃO GUANABARA

somaidade = 0
medidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Fm' and idade < 20:
        totmulher20 += 1
medidade = somaidade / 4
print('A média da idade do grupo é de {} anos.'.format(medidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
'''