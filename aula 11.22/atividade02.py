# faça um programa que, dado um conjunto de N numeros,determine o menor valor
# o maior valor e a soma dos valores.
maior =0
menor =None

while True:
    saida = input('digite "S" para sair: ')
    if saida == 's' or saida == 'S':
        print('volte sempre! ')
        break
    numero = int(input('informe um numero inteiro: '))
    
    if numero> maior:
        maior =numero
    if menor == None or numero <menor:
        menor = numero
print(f' A soma de {maior} + {menor} = {maior+menor}')
print(f'O maior valor é : {maior}')
print(f'O menor valor é: {menor}')