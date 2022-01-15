# Crie um programa que leia dois valores e mostre um menu como ao lado na tela:
# Seu programa deverá realizar a operação solicitada em cada caso.

# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do Programa

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

decisao = 0

while decisao != 5:

    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')

    decisao = int(input('Qual operação deseja fazer com esses números:'))

    if decisao == 1:
        soma = numero1 + numero2
        print('\nVocê escolheu soma, a soma de {} com {} é {}'.format(numero1, numero2, soma))

    elif decisao == 2:
        multiplicacao = numero1 * numero2
        print('\nVocê escolheu multiplicação, a multiplicação entre {} e {} resulta em {}'.format(numero1, numero2, multiplicacao))

    elif decisao == 3:
        if numero1 > numero2:
            print('\nVocê escolheu maior, o número {} é maior que o número {}'.format(numero1, numero2))

        else:
            print('\nVocê escolheu maior, o número {} é o maior que o número {}'.format(numero2, numero1))

    elif decisao == 4:
        numero1 = int(input('Digite um novo número: '))
        numero2 = int(input('Digite outro novo número: '))

    elif decisao > 5:
        print('Este número não faz parte do correspondente ao menu, digite novamente...')

    else:
        print('Voce saiu do programa.')



