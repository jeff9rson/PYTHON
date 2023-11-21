#for trabalha com iteraveis, tem que possuir uma variavel de controle
#iter()
#next()

nome = 'paulo'
texto = iter(nome)
print(next(texto))
print(texto)
for letra in nome:
    print(letra)

for letra in nome:
    print("ok")

lista_nomes = ['joão', 'pedro', 'mateus', 'judas', 'tiago']

lista_enumerada = enumerate(lista_nomes)
print(lista_nomes)
print(lista_enumerada)

for item in lista_enumerada:
    print(item)

for indice_lista, item_lista in enumerate(lista_nomes):
    print(f'{indice_lista} é o {item_lista} da lista')