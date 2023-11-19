alunos01 =int(input ("digite sua idade"))
contador = 0
while contador < 20:
    idade_aluno = int(input("informe sua idade"))
    if idade_aluno > 13:
        print(f'o aluno { contador } tem mais de 13 anos')
    contador += 1