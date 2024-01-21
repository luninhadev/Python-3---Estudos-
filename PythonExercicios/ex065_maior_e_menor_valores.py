'''
DESAFIO 065

Crie um programa que leia varios números inteiros. No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores.
'''

print('{:^45}'.format('Média maior e menor'))
n = []
soma = media = i = 0
start = 1
while start != 0:
    n.append(int(input('Digite um número: ')))
    print(n)
    r = str(input('Quer continuar?\n[S/N]:')).upper()
    if r != 'S':
        start = 0
        maior = n[0]
        menor = n[0]
        for c in range(0, len(n)):
            soma += n[c]
            if n[c] > maior:
                maior = n[c]
            if n[c] < menor:
                menor = n[c]
        media = soma / len(n)
        print('\n')
        print('A média é: {:.2f}\nO maior é: {}\nO menor é: {}'.format(media, maior, menor))
