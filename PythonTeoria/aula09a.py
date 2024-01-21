'''
    MANIPULANDO CADEIAS DE TEXTO
'''
print('''Welcome! Are you completely new to progrmaming?
about why and how to get started with Python, Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
Its also easy for begnners to use and learn, so jumpin!''')
print('\n'*3)

frase = 'Curso em Video Python'
print(frase)

# Fatiar [início : fim : salto]
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[::2])

# count conta quantas vezes tem 'O' na frase e retorna um número.
print(frase.count('O'))
print(frase.upper().count('O')) # joga toda frase em maiúscula e conta quantas vezes tem 'O' na frase e retorna um número

# conta quantas letras tem na frase (os espaços em branco conta também)
print(len(frase))

# O strip() corta os espaços em branco no inicio e no fim.
print(len(frase.strip()))

# Troca a pala 'Python' pela palavra 'Android'.
print(frase.replace('Python', 'Android'))

# Frase é imutável
print(frase[0]) # frase[0] = 'J' >>> isso da erro!

# mudar o conteúdo de um índice
frase = frase.replace('Python', 'Android')
print(frase)

# Verifica se a palavra está dentro da frase e retorna um valor boolean
print('Curso' in frase)

# Verifica em que índice começa a palavra 'Curso' e retorna a posição do índice
print(frase.find('Curso'))

frase = 'Curso em Video Python'

# Cria uma lista apartir dos espaços entre as palavras
print(frase.split())

dividido = frase.split()

# Mostra o primeiro índice da lista
print(dividido[0])

# Mostra terceira letra da terceira palavra ou segundo índice
print(dividido[2][3])

# junta a palavra ou coloca algo nos espaços em branco
print(''.join(dividido))
