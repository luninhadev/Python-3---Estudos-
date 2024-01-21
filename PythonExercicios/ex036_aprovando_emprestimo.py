'''
    DESAFIO 036

    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai
pagar.

    Cacule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''

print('{:_^52}'.format('Empréstimo de ímóvel'))

c = float(input('Digite o valor da casa: R$'))
s = float(input('Digite o seu salário: R$'))
anos = int(input('Em quantos anos você irá pagar: '))
p = float(anos * 12) # número de parcelas
vp = c / p # valor da parcela
ps = s * 0.3 # Porcentagem do salário

if vp <= ps:
    print('\033[34mParabéns!!! Empréstimo aprovado!!!\033[m')
    print('A casa ficou no valor de R${:.2f} '.format(vp).replace('.', ','), end='')
    print('em {:.0f}x'.format(p))
elif vp > ps:
    print('\033[31mEmpréstimo negado\nInfelizmente o valor da parcela ultrapassou o limite de 30% de sua renda...\033[m')
    print('A casa ficou no valor de R${:.2f} em {:.0f}x '.format(vp, p).replace('.', ','))
