# uma lista ela é representada pelos []
# len - metado que retorna a quantidade de itens de uma lista
# obs(todo metado por obrigação ele retorna algum valor)
#obs append -metado que insere valores no fim da lista
#del -remove pelo o indice especifico da lista
#remove - remove um objeto especificado da lista
# pop -remove o ultimo objeto da lista
# insert - ele adiciona um objeto no inicio da lista
lista = []
print(lista)
print(len(lista))
lista = ['front']
print(lista, type(lista))
print(len(lista))
lista = ['back']
print(lista, type(lista))
print(len(lista))
lista.append('data')
print(lista, type(lista))
print(len(lista))

lista = ['back', 'tarde', 21, True, 8.8]
print(f' a quantidade de alunos na turma é:{lista[2]}')
lista[2] = 22
print(lista)
lista[1] =False
print(lista)
lista[1] = ['Neyva', 'Alice', 'lara', 'Paula', 'Geisa']
print(lista[1][2])

del lista[-2]
print(lista)
lista.remove('back')
lista.insert(0,'amontada valley')