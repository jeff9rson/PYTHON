class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.__cpf = None

    def __str__(self):
        return f'nome: {self.nome}, idade:{self.idade} e CPF:{self._cpf}'
    def get_cpf(self):
        return self.__cpf
    def set_cpf(self,meu_cpf):
        self.__cpf = meu_cpf
class professor(Pessoa):
    def __init__(self, nome, idade,salario,disciplina,cpf):
        super().__init__(nome, idade)
        self.salario = salario
        self.disciplina = disciplina
        self. __cpf = cpf
    def __str__(self):
        return f'salario:{self.salario}, disciplina{self.disciplina}'
class aluno(Pessoa):
    pass

paulo = professor('paulo junior',29,1400.00,'back and,')
paulo.set_cpf(123456789)
print(paulo)