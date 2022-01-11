# Crie um programa que leia um nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome separadamente.
# EX: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Digite seu nome completo: ')).strip()

n = nome.split()

print('primeiro = {}'.format(n[0]))
print('último = {}'.format(n[len(n)-1]))