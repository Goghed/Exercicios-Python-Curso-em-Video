# A confederação Nacional de natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria de acordo com a idade:

# Até 9 anos : MIRIM
# Até 14 anos : INFANTIL
# Até 19 anos : JUNIOR
# Até 25 anos : SÊNIOR
# Acima: MASTER

from datetime import date

atual = date.today().year

nascimento = int(input('Ano de nascimento: '))

idade = atual - nascimento

print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')

if idade <= 14:
    print('Classificação: INFANTIL')

if idade <= 19:
    print('Classificação: JUNIOR')

if idade <= 25:
    print('Classificação: SÊNIOR')

else:
    print('Classificação: MASTER')
