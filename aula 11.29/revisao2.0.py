#estruturas condicionadas
variavel = 20
if variavel <20:
    print('menor que 20')
elif variavel == 20:
    print('igual a  20')
elif variavel == 20:
    print('está no intervalo entre 21 e 49')
else:
    print('qualquer outra coisa')

# estruturas de repetição
# for e WHILE


for i in range(10):
    print(f' print o numero {i}')

contador = 5
while contador > 0:
    print(f'esse é o print do numero {contador}')
contador -= 1

# join - unir strings
lista =['joao','paulo','II']
nome = '-'.join(lista)
print(nome)