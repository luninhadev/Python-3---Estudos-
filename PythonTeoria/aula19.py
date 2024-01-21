pessoas = {'nome': 'Gustavo', 'sexo': 'F', 'idade': 26}
print(pessoas)
print(pessoas['nome'])
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items()) # Uma lista com três Tuplas dentro
for k in pessoas.keys():
    print(k)
# del pessoas['sexo']
pessoas['nome'] = 'Luna'
pessoas['peso'] = 58.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
for k in pessoas.values():
    print(k)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'silga': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado3 = dict()
brasil1 = list()
for c in range(0, 3):
    estado3['uf'] = str(input('Unidade Federativa: '))
    estado3['sigla'] = str(input('Sigla do Estado: '))
    brasil1.append(estado3.copy()) #Não pode usar [:] para copiar um dicionário!!!
for e in brasil1:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
for e in brasil1:
    for v in e.values():
        print(v, end=' ')
    print()
