from random import shuffle
#o metodo split() separa uma string em uma lista e os elementos são separados por espaço
#o shuffle embaralha os elementos da lista
Alunos = 'B4RB4BR4NC4 Gustf Wannted Gustavo'.split()
shuffle(Alunos)
print('A ordem de apresentação será : {}'.format(Alunos))
