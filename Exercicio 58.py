# Melhore o jogo do desafio 28 onde o computador vai pensar em um número de 0 a 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

import random

numeroEscolhido = 0
contador = 0

numeroPc = random.randint(1, 10)

while numeroEscolhido != numeroPc:
    numeroEscolhido = int(input('Digite o número escolhido: '))
    contador += 1

if numeroEscolhido == numeroPc:
    print('\nParabéns você acertou o número escolhido')
    print('\nNumero escolhido: {}'.format(numeroPc))
    print('\nPara acertar você digitou {} vezes'.format(contador))

