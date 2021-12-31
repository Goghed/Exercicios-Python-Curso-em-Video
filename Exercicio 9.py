# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

numero = int(input('Digite um número: '))
quantidade = 0

print('A tabuada do {} é: \n'.format(numero))

for quantidade in range( 0, 11):
    multiplicacao = numero * quantidade
    print('{} x {} = {}'.format(numero, quantidade, multiplicacao))
