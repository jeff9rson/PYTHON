# count - função é contar quantas vezes o caractere aparece em ums string
# upper e a lower - dois metados que deixam a strinng toda em MAISCULA ou a string toda em MINUSCULA
#find -busca por uma expresão dentro da frase
#Replace - é utilizado para realizar alterações dentro das strings
#capitalize - deixa a primeira letra da palavra minuscula
# splir -transforma a sua string em uma lista
frase = "A banana é amarela e o abacate é verde.".lower()
letra = 'a'
print(f'A letra " {letra} " aparece {frase.count(letra)} vezes na frase "{frase}" ')
print(frase.find('ana'))
achei = frase.find('roxo')
if achei >=0:
    print(f'A expressão foi encontrada no indice{achei}')
else:
    print(f'A expressão foi encontrada')

nova_frase = frase.replace('banana','maracuja')
nova_frase1 = frase.replace('abacate', 'manga')

print(frase)
print(nova_frase)
print(nova_frase1)
print(frase.capitalize())