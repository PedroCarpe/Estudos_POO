from classe_pessoa import ClassePessoa

class Estudante(ClassePessoa):
    def __init__(self,nome,email,telefone,cpf,curso,periodo,disciplinas,nivel,status):
        ClassePessoa.__init__(self,nome,email,telefone,cpf)
        self.curso = curso;
        self.periodo = periodo;
        self.disciplinas = disciplinas;
        self.nivel = nivel;
        self.status = status;
    

    def __str__(self):
        return f'\n\n__Dados_do_Estudante__\n\nNome: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}\nCurso: {self.curso}\nPeríodo: {self.periodo}\nDisciplinas: {self.disciplinas}\nNível: {self.nivel}\nStatus: {self.status}'

