class automovel:
    def __init__(self,placa= 'XYZ-4925'):
      self.placa = placa
    def __get_placa(self):
       return self.placa
    def Dirigir(self,velocidade):
       print(f'estou dirigindo a {velocidade} km/h')

carro = automovel()
print(carro.__get_placa())
carro.Dirigir()
moto = automovel()
