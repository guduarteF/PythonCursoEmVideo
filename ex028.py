import random
from time import sleep

num = random.randrange(0,6) #randint , também funciona

advinhar = int(input('Tente adivinhar em qual número eu pensei de 0 a 5: '))
print('PROCESSANDO . . .')
sleep(2)
print('VENCEU ! Você acertou o número' if num == advinhar else 'PERDEU , O número que eu pensei foi {}'.format(num))
