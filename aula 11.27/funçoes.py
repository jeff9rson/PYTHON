# funções são blocos de nde codigos que são executadas somente quando são chamados
# parametro : def
# obs - as funções devem ter prioridade no codigo

def media(nota,nota2,nota3):
    media =(nota01 + nota02 + nota03) /3
    return media




nota01 = int(input('informe a primeira nota: '))
nota02 = int(input('informe a segunda nota: '))
nota03 = int(input('informe a terceira nota:'))
media(nota01,nota02,nota03)
print(media(nota01,nota02,nota03))

def calcula_horas_extras(quantidade_horas,valor_hora):
    horas = float(quantidade_horas)
    taxa = float(valor_hora)

    if horas >= 40:
        valor_receber = (horas - 40) * taxa
    return valor_receber

quantidade_horas = float(input('informe o total de horas trabalhadas: '))
valor_da_hora = float(input('informe o valor da taxa do colaborador'))
print(calcula_horas_extras(quantidade_horas,valor_da_hora))

salario = 1400.00
print(salario + calcula_horas_extras(quantidade_horas,valor_da_hora))

#faça um programa, com uma função que necessite de um argumento. a função retorna o valor de caracter 'p'
# a função retorna o caractere