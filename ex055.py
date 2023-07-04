""" Faça um programa que leia o peso de cinco pessoa.
No final , mostre qual foi o maior e o menor peso lidos"""
pesoMenor = 1000
pesoMaior = 1
for c in range(1, 6):
    peso = float(input('Digite um peso '))
    if peso > pesoMaior:
        pesoMaior = peso
    elif peso < pesoMenor:
        pesoMenor = peso

print('O peso menor é {}'.format(pesoMenor))
print('O peso maior é {}'.format(pesoMaior))