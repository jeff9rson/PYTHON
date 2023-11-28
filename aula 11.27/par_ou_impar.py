jogador1 = input("escolha par ou impar").lower()
if jogador1 == 'Par':
    jogador2 = 'Impar'
else:
    jogador2 = 'Par'

numero_jogador1 = int(input('escolha seu numero'))
numero_jogador2 = int(input('escolha seu numero'))

resultado = numero_jogador1 + numero_jogador2
if resultado % 2 ==0:
    if jogador1 == 0:
        print("jogador 1. You Win")
    else:
        print("jogador 2. You Loser")
else:
    if jogador1 == 'impar':
        print(" jogador 2.  You Win")
        

