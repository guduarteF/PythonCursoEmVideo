""" Escreva um programa que leia um valor em metros e o exiba
convertido em centimetro e milimetros"""

metros = float(input('Digite uma distância em metros'))
centimetro = metros * 100
milimetros = metros * 1000
print('A distância em centimetro é {:.0f} e em milimetros {:.0f}'.format(centimetro,milimetros))