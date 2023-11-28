# condição ternaria acontece em formato de linha

salario = float(input('informe o valor do seu salario'))
if salario >= 2500.00:
    print("IR será cobrado")
else:
    print('ir não sera cobrado')
variavel_controle = 'IR será cobrado' if salario >= 2500.00 else 'IR não sera cobrado'
print(variavel_controle)

vr_controle = 'OK 1' if False else 'ok 2' if True else 'fim'
print(vr_controle)