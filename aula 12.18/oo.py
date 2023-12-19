class Estudante:
    nome = 'paulo'
    matricula = 353637
class EstudanteGraduacao(Estudante):
    curso = 'ADS'
    def __str__(self):
        return f'nome: {self.nome},
        matricula:{self.matricula} e curso:{ self.curso}'
class EstudantePos(Estudante):
    nivel = 1
    orientador = 'Prof Carlos Alberto'

aluno= EstudanteGraduacao()
print(f'ola,{aluno.nome}seu curso de guaduação é{aluno.curso} e sua matricula de acesso é{aluno.matricul}')

aluno2= EstudantePos()
print(f'ola,{aluno2}seu nivel é {aluno2} é {aluno2.nivel} e tutor será o {aluno2.orientador}')


