
class ClassePessoa:

    def __init__(self,nome,email,telefone,cpf):
        self.nome = nome;
        self.email = email;
        self.telefone = telefone;
        self.cpf = cpf;


    def __str__(self):
        return f'\n\n__Dados_do_Usuário__\n\nNome: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}\nCPF: {self.cpf}' 
       
