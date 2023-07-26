""" Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex. Escreva('Olá, Mundo!')
Saída:   ~~~~~~
        Ola Mundo!
        ~~~~~~~     """

def MensagemPersonalizada(msg):
    num = len(msg)
    print('~' * num)
    print(msg)
    print('~' * num)


MensagemPersonalizada('Gustavo Guanabara')
MensagemPersonalizada('Curso de Python no YouTube')
MensagemPersonalizada('CeV')
