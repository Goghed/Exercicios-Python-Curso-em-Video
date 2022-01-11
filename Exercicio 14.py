# Escreva um programa que converta uma temperatura digitada em °C e converta para °F

temperatura = float(input('Digite a temperatura em graus °C: '))

convertido = (temperatura * 1.8) + 32

print('A temperatura de {}ºC é {}°F em Fahrenheit'.format(temperatura, convertido))
