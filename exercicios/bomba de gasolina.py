class BombaGasolina:
    def __init__(self, quantidade_combustivel):
        self.tipo_combustivel = None
        self.valor_combustivel = 0
        self.valor_pagar = 0
        self.quantidade_combustivel = quantidade_combustivel
    def set_tipo_combustivel(self):
        self.tipo_combustivel = input('Digite o tipo de combustivel, "Alcool ou Gasolina": ').lower()
        if self.tipo_combustivel == 'alcool':
         self.valor_combustivel = 4.50
        elif self.tipo_combustivel == 'gasolina':
         self.valor_combustivel = 6.30
    def escolha_cliente(self):
       escolha= input('você deseja abastecer em litros ou dinheiro?')
       if escolha == 'litros':
          self.abastecer_litro
       elif escolha == 'dinheiro':
          self.abastecer_dinheiro() 
    def abastecer_litro(self):
       litro = float('Digite a quantidade de litros:')
       self.valor_pagar = litro * self.valor_combustivel
       print(f'você vai pagar R$ { self.valor_pagar} em {litro} litros')
    def