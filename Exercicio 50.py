# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o

pares = 0
contador = 0

for numeros in range(0, 6):
    numero = int(input('Digite o {}º número: '.format(numeros+1)))

    if numero % 2 == 0:
        pares += numero
        contador += 1

print('A soma de todos os {} números pares digitados é {}'.format(contador, pares))