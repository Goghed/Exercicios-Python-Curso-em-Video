# Crie um programa que leia um número Real qualquer pelo teclado e mostre a tela sua porção inteira

# Ex: Digite um número: 6.127
# o número 6.127 tem a parte inteira 6

import math

numero = float(input('Digite um número: '))

inteiro = math.trunc(numero)

print('O número {} tem a parte inteira {}'.format(numero, inteiro))