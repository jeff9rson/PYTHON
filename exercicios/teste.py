#faça um programa utilizando o while que mostre na tela de 0 ate n,em que n é o limite 
#inserido pelo o usuario

# variaveis
numero = int(input("informe um numero "))
#contador do while
contador = 0

'''Enquanto o contador for menor ou igual ao numero que o usuário pediu'''
while contador<=numero:
    #aqui vai mostrar o contador indo ate o numero que o usuaerio pediu:
    print(contador)
    #aqui é para o contador rodar de passo a passo, 1 passo por vez até a condição deixar 
    # de ser verdade 
    contador += 1