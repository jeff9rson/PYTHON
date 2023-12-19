class pet:
    def __init__(self,nome,peso):
        self.nome = nome
        self.peso = peso
        self.fome = 0
        self.sede = 0
        self.comida = 0
    #GET
    def get_nome(self):
        return self.nome
    
    def get_fome(self):
        return self.fome
    
    def get_sede(self):
        return self.sede
    
    def get_peso(self):
        return self.peso
    
    def set_nome(self,novo_nome):
        self.nome = novo_nome
    
    def set_peso(self,novo_peso):
        self.peso = novo_peso
    
    def set_sede(self,novo_sede):
        self.peso = novo_sede
    
    def set_fome(self,novo_fome):
        self.peso = novo_fome
        if novo_fome>= 99 or self.fome >=99:
            print(f'Alimente a/o {self.nome}')
            nova_comida = input('quanto de comida você quer á comida para seu pet?')
            self.fome = novo_fome
    
    
