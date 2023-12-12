# CRUD - Created, Readed, Updated e Deleted
dic = { 'nome': 'paulo'} # created
dic2 = dict(idade=23) # created

dic['nome'] # readed
reading = dic.get('nome') #readed

dic.update(sobrenome ='Junior') #updated
dic.update({'idade': 23})
tupla = ('peso', 72.12),
lista = ['data', '13/04/1996']

dic.clear() # deleted
dic.update(lista)

print(dic)
print(dic2)