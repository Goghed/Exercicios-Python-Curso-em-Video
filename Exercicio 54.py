# Crie um programa que leia o ano de nascimento de sete pessoas, no final mostre quantas pessoas ainda não
# atingiram a maioridade e quantas ja são maiores.

from datetime import date

atual = date.today().year
contadorMaior = 0
contadorMenor = 0

for idades in range(0, 7):
    nascimento = int(input('Em que ano a pessoa nasceu: '))
    idade = atual - nascimento

    if idade >= 21:
        contadorMaior += 1

    else:
        contadorMenor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(contadorMaior))
print('Ao todo tivemos {} pessoas maiores de idade'.format(contadorMenor))

