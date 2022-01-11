# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens até 200KM
# e R$ 0,45 para viagens mais longas.

distancia = int(input('Digite a distância da sua viagem: '))

if distancia <= 200:
    valor = distancia * 0.50
    print('O valor da sua viagem será de R$ {}'.format(valor))

else:
    valor = distancia * 0.45
    print('O valor da sua viagem será de R$ {}'.format(valor))
