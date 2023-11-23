# faça um programa que peça um numero inteiro e determine se ele é ou não
# um numero primo. um numero primo é aquele que é divisivel por ele mesmo e por 1

# 1 2 3 4 5 6 7 8 9 10 11

numero = int(input('favor informar um numero inteiro: '))
intervalo = range(1, numero+1)
contador =0
for i in intervalo:
    if numero % i == 0:
        print(f'foi divisivel por {i}')
        contador += 1
if contador ==2:
    print(f'O numero {numero} é primo')
