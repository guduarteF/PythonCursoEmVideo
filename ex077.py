""" Crie um programa que tenha uma tupla com várias palavras ( não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais"""
vogal = ' '
palavras = ('python', 'java', 'ruby', 'csharp', 'typescript', 'django', 'portugol')
count = 0
# guanabara utilizou :

""" for p in palavras:
        print palavra
        for letra in p:
            if letra in 'aeiou':
            print letra"""

for x in range(0, len(palavras)):
    print(f'\n Na palavra {palavras[x]} temos ',end='')
    for y in range(0, len(palavras[x])):
        if 'a' in palavras[x][y]:
            print(palavras[x][y], end=' ')
        if 'e' in palavras[x][y]:
            print(palavras[x][y], end=' ')
        if 'i' in palavras[x][y]:
            print(palavras[x][y], end=' ')
        if 'o' in palavras[x][y]:
            print(palavras[x][y], end=' ')
        if 'u' in palavras[x][y]:
            print(palavras[x][y], end=' ')

