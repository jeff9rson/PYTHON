while True:
    nota = int(input('digite uma nota:'))
    if nota <0 or nota >10:
        print('nota invalida')
    elif nota >=0 and nota<=10:
        break