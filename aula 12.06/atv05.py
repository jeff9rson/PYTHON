# 5.vamos criar um sistema de login e senha. crie um dicionario contendo os acessos 
# dos colaboradores com nome de usuario e senha. em seguida peça as informações e valide o 
# login do usuario.

dic_acessos = {'Paulo': '123456', 'joao': '121212'}
usuario_senha = {}
usuario = input('informe seu USUARIO: ')
senha = input ('informe sua senha')

usuario_senha[usuario]
print(usuario_senha)

for chave in dic_acessos.keys():
    print(chave)
    if chave == usuario:
        print('Usuario Ok')
        if dic_acessos[chave] == senha:
            print("Acesso Liberado!")
            break
    else:
        print(f'Senha incorreta para o usuario {usuario}')
else:
    print('Usuario')
