entrada = input ('[E] para entrar e [S] para passar: ')
senha_digitada = input("digite a senha de acesso")
senha = "12345678"

if(entrada == "E" or entrada =="e"):
    if (senha == senha_digitada):
        print ("sucesso,você entrou")
    else:
        print("você não entrou,senha INCORRETA")
elif (entrada == 'S' or entrada == 's'):
    if(senha == senha_digitada):
        print("sucesso, você passou")
    
else:
     print("você não passou, senha INCORRETA")