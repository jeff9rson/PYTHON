# alguns cuidados com dados mutaveis
# mutaveis - são dados que podem ter seu valor alterado na memoria do dispositivo
# imutaveis são dados que só podem ser copiados da memoria do dispositivo

lista = ['João', 'paulo']
lista[1] = 'Jose'
print(lista)

nome = 'paulo'
# nome = 'João'
# nome[2] = 'a'
novo_nome = nome
nome = 'João'
print(nome)
print(novo_nome)

lista_a = ['João', 'paulo']
lista_b = lista_a.copy()
lista_b[1] = 'José'
print(lista_a)
print(lista_b)