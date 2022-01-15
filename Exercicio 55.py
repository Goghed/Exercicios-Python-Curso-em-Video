# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor pesos lidos.

maiorPeso = 0
menorPeso = 0

for pessoas in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoas)))

    if pessoas == 1:
        maiorPeso = peso
        menorPeso = peso

    else:
        if peso > maiorPeso:

            maiorPeso = peso

        if peso < menorPeso:

            menorPeso = peso

print('O maior peso digitado foi {}'.format(maiorPeso))
print('O menor peso digitado foi {}'.format(menorPeso))
