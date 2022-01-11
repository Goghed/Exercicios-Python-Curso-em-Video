# Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos digitos separados
# EX: Digite um número: 1834 e mostre da seguinte forma:
# unidade: 4 dezena: 3 centena: 8 milhar: 1

numero = int(input('Informe um número: '))

n = str(numero)

print('Você digitou o número {}'.format(numero))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
