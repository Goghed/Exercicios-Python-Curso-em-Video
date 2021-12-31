# Crie um programa que leia quanto dinheiro uma pessoa tem
# na carteira e mostre quantos Dólares ela pode comprar.

carteira = float(input('Digite o valor que você tem na carteira: '))

cotacaoAtual = 5.54
dolar = carteira / cotacaoAtual

print('Você tem {} na carteira e com a cotação atual que é {}, você consegue comprar {} dolares.'.format(carteira, cotacaoAtual, dolar))


