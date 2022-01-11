# refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for

numero = int(input('Digite um número para ver sua tabuada: '))

print('\nTabuada do {}\n'.format(numero))

for tabuada in range(1, 11):
    multiplicacao = numero * tabuada
    print('{} x {} = {}'.format(tabuada, numero, multiplicacao))
