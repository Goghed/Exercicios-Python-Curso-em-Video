# Escreva um programa que leia um valor em metros e o exiba convertido
# em centimetros e milimetros.

medida = float(input('Digite a medida em metros para ser convertida: '))

centimetros = medida / 100
milimetros = medida / 1000

print('Você digitou {} metros e esse valor em centimetros é {} e em milimetros é {}' .format(medida, centimetros, milimetros))
