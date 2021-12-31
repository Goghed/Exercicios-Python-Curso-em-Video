# Crie um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possiveis sobre ele.

algo = input('Digite algo: ')

print('O tipo primitivo desse valor é  ', type(algo))
print('Só tem espaços? ', algo.isspace())
print('É númerico? ', algo.isnumeric())
print('É alfanumérico?', algo.isalnum())
print('Está em maiusculas?', algo.isupper())
print('Está em minusculas', algo.islower())
print('Está capitalizada?', algo.istitle())
