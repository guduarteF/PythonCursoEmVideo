""" Faça um programa que leia um número inteiro e diga se ele é
ou não um número primo."""

print('Vamos descobrir se um número é PRIMO ou não : ')
print('Para um número ser primo ele :')
print('DEVE ser APENAS divisíveis por 1 e por ele mesmo')
num = int(input('Digite um número :'))
somatorio = 0
for c in range(1, num + 1):
    if num % c == 0:
        somatorio += 1

if somatorio == 2:
    print('O número {} é PRIMO'.format(num))
else :
    print('O número {} NÃO é PRIMO'.format(num))