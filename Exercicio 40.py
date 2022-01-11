# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# média abaixo de 5.0: Reprovado
# média entre 5.0 e 6.9: Recuperação
# média 7.0 ou superior: Aprovado

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

print('Primeira nota {}, segunda nota {} a média é {}'.format(nota1, nota2, media))

if media >= 7:
    print('Parabéns você foi aprovado!')

elif media <= 6.9 and media >= 5:
    print('Você está de recuperação e precisa estudar mais!')

else:
    print('Você está reprovado!')