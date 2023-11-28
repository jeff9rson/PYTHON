from random import randint
placar_jogador =0
placar_computador =0
while True:
    jogador = input('escolha par ou impar').lower()
    
    numero_jogador = int(input('escolha seu numero: '))
    numero_computador = randint(0, 10)
    resultado = numero_jogador + numero_jogador
    if resultado % 2 == 0:
        if jogador == 'par':
            print(f'você ganhou com o numero {numero_jogador}!')
            placar_jogador = placar_jogador +1
        else:
            print(f'O computador ganhou com o numero {numero_jogador}')
            placar_computador = placar_jogador +1
    else:
        if jogador == 'impar':
            print(f'você ganhou com o numero {numero_jogador}!')
        else:
            print(f'computador ganhou com o numero {numero_jogador}!')
            placar_computador = placar_jogador +1
        saida = input('Digite [S] para Sair').upper
        if saida == 'S':
            if placar_computador > placar_jogador:
                confirma_saida = input('você esta perdendo. tem certeza que vai sair FRANGO. digite "coco" ').lower()
                if confirma_saida == 'coco':
                    print("volte sempre")
                    break
                else:
                    continue
                  