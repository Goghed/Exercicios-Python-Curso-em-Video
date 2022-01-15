# Crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsiderando os espaços.

frase = str(input('digite a sua frase: ')).strip().upper()

palavras = frase.split()

junto = ''.join(palavras)

inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('Essa frase é um Palíndromo!')
else:
    print('Essa frase não é um palíndromo')

print('Você digitou a frase: - {} e o inverso dela é {}'.format(frase, inverso))



