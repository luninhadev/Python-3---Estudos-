'''
    DESAFIO 040

Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida:
    - Média abaixo de 5.0: REPROVADO.
    - Média entre 5.0 e 6.9: RECUPERAÇÃO.
    - Média 7.0 ou superior: APROVADO.
'''

print('-' * 8, 'Média do aluno', '-' * 8)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = float((n1 + n2) / 2)

if media < 5.0:
    print('\033[31mREPROVADO!\033[m')
elif (media > 5.0) and (media <= 6.9):
    print('\033[33mRECUPERAÇÃO!\033[m')
elif media >= 7.0:
    print('\033[32mAPROVADO!!!\033[m')
print('-' * 32)
