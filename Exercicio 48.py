# Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram
# no intervalo de 1 e 500.

soma = 0
contador = 0

for numeros in range(1, 501, 2):

    if numeros % 3 == 0:

        soma = soma + numeros
        contador += 1

print('A soma dos números impares multiplos de 3 é {} e foram somados {} números'.format(soma, contador))

