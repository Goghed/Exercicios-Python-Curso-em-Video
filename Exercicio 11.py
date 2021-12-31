# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pinta-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura

metros = area / 2

print('A sua parede tem uma área de {} metros² e para pinta-la você precisa de {} litros de tinta'.format(area, metros))