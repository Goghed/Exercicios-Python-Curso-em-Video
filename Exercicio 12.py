# Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço com 5% de desconto

valor1 = float(input('Digite o valor do produto: '))

desconto = valor1 - (valor1 * 0.05)

print('O valor do produto com 5% de desconto é {}'.format(desconto))