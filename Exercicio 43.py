# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
# - abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Informe seu peso (KG): '))
altura = float(input('Informe a sua altura: '))

imc = peso / (altura ** 2)

print('O imc é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Está Abaixo do peso')

elif imc >= 18.5 or imc < 25:
    print('Está no peso ideal')

elif imc >= 25 or imc < 30:
    print('Está com sobrepeso')

elif imc >= 30 or imc < 40:
    print('Está com obesidade')

elif imc >= 40:
    print('Está com obesidade morbida')
