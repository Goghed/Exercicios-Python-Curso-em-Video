# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex: 5 = 5x4x3x2x1=120

from math import factorial

numero = int(input('Digite um número para achar mostrar seu fatorial: '))

fatorial = factorial(numero)

print('O fatorial de {} é {}'.format(numero, fatorial))
