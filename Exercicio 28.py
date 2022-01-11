# Escreva um programa que faça o computador pensar em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numeroEscolhido = int(input('Digite o número escolhido: '))

numeroPc = random.randint(0, 5)

if numeroEscolhido == numeroPc:
    print('\nParabéns você acertou o número escolhido')
    print('\nNumero escolhido: {}'.format(numeroPc))

else:
    print('\nQue pena, você errou, tente novamente!')
    print('\nNumero escolhido: {}'.format(numeroPc))
