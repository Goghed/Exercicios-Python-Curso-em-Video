# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math

numero = int(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raiz = math.sqrt(numero)

print('O número digitado foi {}, o dobro desse número é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(numero, dobro, triplo, raiz))
