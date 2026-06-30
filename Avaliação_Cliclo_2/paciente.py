#Classe Pai - Super Class
# Nome 
# data_nascimento
# CPF
# telefone
# tipo sanguíneo
# numero_prontuario
# exibir_informacoes() -> que mostra os dados da pessoa.
class Paciente: 
    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario): #Método cosntrutor
        
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._telefone = telefone
        self._tipo_sanguineo = tipo_sanguineo
        self._numero_prontuario = numero_prontuario


    def registrar_atendimento(self, tipo, custo):
        print(f"Confirmação de atendimento para o(a) paciente {self._nome}:")
        print(f"Tipo de atendimento: {tipo} Custo do atendimento: R$ {custo:.2f}")
    
    
    def exibir_informacoes(self, detalhado ):

        if detalhado == True:
            print(f"Nome:{self._nome}")
            print(f"Data_nascimento: {self._data_nascimento}")
            print(f"CPF: {self._cpf}")
            print(f"Telefone: {self._telefone}")
            print(f"Tipo Sanguíneo: {self._tipo_sanguineo}")
            print(f"Número do prontuário: {self._numero_prontuario}")

        else: 
            print(f"Nome: {self.nome}")
            print(f"Tipo Sanguíneo: {self._tipo_sanguineo}")
            print(f"Número do prontuário: {self._numero_prontuario}")
            

       
        

