""" Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
no final , de acordo com a média atingida:

- Média abaixo de 5.0 REPROVADO
-Média entre 5.0 e 5.9 RECUPERAÇÃO
-Média 7.0 ou superior APROVADO """

nota1 = float(input('Qual foi a primeira nota do aluno : '))
nota2 = float(input('Qual foi a segunda nota do aluno : '))
media = (nota1 + nota2) / 2

print('Sua média foi {}'.format(media))
if media >= 7:
    print('Você está \033[4;32m APROVADO \033[m')
elif 5 <= media >= 5.9:
    print('Você está de \033[4;33m RECUPERAÇÃO \033[m ')
else:
    print('Você está \033[4;31m REPROVADO \033[m')
