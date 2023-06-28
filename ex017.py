from math import sqrt

co = float(input('Qual o comprimento do cateto oposto ? '))
ca = float(input('Qual o comprimento do cateto adjacente ? '))
h = sqrt((co ** 2 + ca ** 2))
print('O comprimento da hipotenusa é {:.2f} '.format(h))
