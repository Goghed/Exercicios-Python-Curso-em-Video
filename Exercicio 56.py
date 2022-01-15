# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos.

somaIdades = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totalMulher20 = 0

for pessoas in range(1, 5):

    nome = str(input('Digite o nome da {}ª pessoa: '.format(pessoas)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(pessoas)))
    sexo = str(input('Digite o sexo da {}ª pessoa - [M/F]: '.format(pessoas)))

    somaIdades += idade

    if pessoas == 1 and sexo == 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome

    if sexo in 'Mn' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome

    if sexo in 'Ff' and idade < 20:
        totalMulher20 += 1

mediaIdade = somaIdades / pessoas

print('A média de idade do grupo é de {}'.format(mediaIdade))
print('O homem mais velho chama {} e tem {} anos.'.format(nomeVelho, maiorIdadeHomem))
print('E temos {} mulheres com idade abaixo de 20 anos'.format(totalMulher20))
