# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do
# tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year

nascimento = int(input('Qual seu ano de nascimento: '))

idade = atual - nascimento

print('Quem nasceu em {} tem {} anos em {}'. format(nascimento, idade, atual))

if idade == 18:
    print('Você tem que fazer o alistamento IMEDIATAMENTE!')

elif idade < 18:
    faltando = idade - 18
    ano = atual - faltando
    print('Ainda faltam {} anos para o alistamento'.format(faltando))
    print('Seu alistamento será em {}'.format(ano))

elif idade > 18:
    faltando = idade - 18
    ano = atual - faltando
    print('Você já deveria ter se alistado há {} anos.'.format(faltando))
    print('Voce se alistou em {}'.format(ano))
