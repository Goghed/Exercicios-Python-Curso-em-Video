# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condições de pagamento:
# a vista dinheiro/cheque: 10% de desconto
# a vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' Lojas Guanabara '))

preco = float(input('Preço das compras: R$ '))

print(''' Formas de Pagamento
[1] à vista no dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

escolha = int(input('Escolha sua opção: '))

if escolha == 1:
    total = preco - (preco * 0.10)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preco, total))

elif escolha == 2:
    total = preco - (preco * 0.05)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preco, total))

elif escolha == 3:
    total = preco
    parcela = preco / 2
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final e será parcelado em 2x de R$ {:.2f}'.format(preco, total, parcela))


elif escolha == 4:
    total = preco + (preco * 0.20)
    parcela = total / 3

    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final e será parcelado em 3x de R$ {:.2f}'.format(preco, total, parcela))


