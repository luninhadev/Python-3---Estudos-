teste = list()
teste.append('Luna')
teste.append(26)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)

pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoas)
print(pessoas[0])
print(pessoas[0][0])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')

grupo = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    grupo.append(dado[:]) #Importante colocar [:] pra ele copiar o valor qu o usuário digitou
    dado.clear()
print(grupo)
