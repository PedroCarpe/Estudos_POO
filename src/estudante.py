from classe_pessoa import ClassePessoa
from disciplina import Disciplina

class Estudante(ClassePessoa,Disciplina):
    def __init__(self,nome,email,telefone,cpf,curso,periodo,nome_disciplina,codigo,carga_horaria,media_aluno,nivel,status):
        ClassePessoa.__init__(self,nome,email,telefone,cpf)
        Disciplina.__init__(self,nome_disciplina,codigo,carga_horaria,media_aluno,frequencia=None)
        self.curso = curso;
        self.periodo = periodo;
        #self.disciplinas = disciplinas;
        self.nivel = nivel;
        self.status = status;
    
    #como implementar uma média, para cada disciplina?

    def __str__(self):
        return f'\n\n__Dados_do_Estudante__\n\nNome: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}\nCurso: {self.curso}\nPeríodo: {self.periodo}\nNível: {self.nivel}\nStatus: {self.status}\n\n__Disciplinas__ \n {Disciplina._str_(self)}'

