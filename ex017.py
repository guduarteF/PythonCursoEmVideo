""" Faça um programa que leia o comprimento do cateto oposto e
do cateto adjacente de um triangulo retangulo , calcule e mostre o
comprimento da hipotenusa"""

from math import sqrt

co = float(input('Qual o comprimento do cateto oposto ? '))
ca = float(input('Qual o comprimento do cateto adjacente ? '))
h = sqrt((co ** 2 + ca ** 2))
print('O comprimento da hipotenusa é {:.2f} '.format(h))
