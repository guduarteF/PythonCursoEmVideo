""" Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno , cossseno e tangente desse angulo"""

from math import sin, cos, tan, radians
ang = float(input('Digite o angulo que você deseja ? '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang,seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))
