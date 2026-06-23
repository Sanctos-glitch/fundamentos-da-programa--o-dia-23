from pessoa import Pessoa
# NOME, CPF, DATA DE NASCIMENTO, ANO DE INGRESSO, NOTAS, MATRICULA E SE ESTAR ATIVO OU NÃO
class Aluno(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, ano_ingresso: int, matricula: str):
        super().__init__(nome, cpf, data_nascimento)
        self.ano_ingresso = ano_ingresso
        self.matricula = matricula
        self. ativo = True
        self.notas = []

    # metodos de Notas
    def adicionar_notas(self, disciplina: str, nota: float):
    # nota esteje entre 0 e 10
        
    #se eu preciso verificar se esta entre 0 e 10 então eu preciso fazer uma condicional entre essas notas.

        if not(0 <= nota <= 10):
           raise ValueError("Nota deve estar entre 0 e 10.")

        if disciplina not in self.notas :
            self.notas[disciplina] = []

        self.notas[disciplina].append(nota)