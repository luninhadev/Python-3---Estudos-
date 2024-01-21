'''
DESAFIO 031

Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
Km para viagemde até 200Km e R$0,45 para viagens mais longas
'''

print('-' * 8, 'Preço da viagem', '-' * 8)
km = int(input('Quantos km é a viagem: '))

if km <= 200:
    print('O custo da viagem ficou em R${:.2f}'.format(km * 0.50).replace('.', ','))
else:
    print('O custo da viagem ficou em R${:.2f}'.format(km * 0.45).replace('.', ','))