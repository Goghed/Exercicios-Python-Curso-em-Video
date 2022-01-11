# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada KM acima do limite.

velocidade = int(input('Digite a velocidade do veiculo: '))

limite = 80

if velocidade > limite:
    multa = (velocidade - limite) * 7
    print('Voce passou do limite de velocidade, sua multa terá o valor de R$ {} '.format(multa))
else:
    print('Dentro do limite permitido.')
