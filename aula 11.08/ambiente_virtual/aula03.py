#operadores IN e NOT IN

nome = "jefferson"
print('je' in nome)

print('='*20)

seu_nome = input ('informe seu nome: ')
buscar = input ('informe o valor a ser encontrado')

if(buscar in seu_nome):
     print(f' {buscar} está contido em{seu_nome}')



nao_nome ="joãozinho"
print("ão" not in nao_nome)