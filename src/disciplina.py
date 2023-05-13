class Disciplina:
    def __init__(self,nome_disciplina,codigo,carga_horaria,media_aluno,frequencia=None):
        self.nome_disciplina = nome_disciplina;
        self.codigo = codigo;
        self.carga_horaria = carga_horaria;
        self.media_aluno = media_aluno;
        self.frequencia = frequencia;

    def _str_(self):
        return f'\nNome: {self.nome_disciplina}\nCódigo: {self.codigo}\nCarga Horária: {self.carga_horaria}\nMédia Aluno: {self.media_aluno}\nFrequência: {self.frequencia}'    