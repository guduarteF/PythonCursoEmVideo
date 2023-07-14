""" Crie um programa que vai ler vários números e colocar uma lista.
Depois disso , crie duas listas extras que vão conter apenas os valores pares
e os valores impares digitados,respectivamente.
Ao final mostre o conteúdo das três listas geradas."""
continuar = 'S'
valores = list()
while True:
    if continuar == 'S':
        num = int(input('Digite um número: '))
        valores.append(num)
        continuar = str(input('Quer continuar ? ')).strip().upper()
    else:
        break
print(f'A lista completa é : {valores}')
parvalores = list()
imparvalores = list()
for pos, valor in enumerate(valores):
    if valores[pos] % 2 == 0:
        parvalores.append(valores[pos])
    else:
        imparvalores.append(valores[pos])
print(f'A lista de pares é {parvalores}')
print(f'A lista de ímpares é {imparvalores}')
