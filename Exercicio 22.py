# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao total ( sem considerar espaços)
# Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')

print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem um total de {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))