from paciente import Paciente
# PacienteConvenio: subclasse classe filha
# Pagamento em plano de saúde
# Atributo:nome_convenio, numero_carteirinha
# Método sobrescrito: exibir_informacoes()
# exibir_informacoes()


class PacienteConvenio(Paciente): 
    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario, nome_convenio, numero_carteirinha):
        
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)


        self._nome_convenio = nome_convenio
        self._numero_carteirinha = numero_carteirinha


    def registrar_autorizacao(self, procedimento, valor_recusado):
        
        print(f"Procedimento Autorizado: {procedimento}")
        print(f"Valor Recusado pelo Plano: R$ {valor_recusado:.2f}")

    def exibir_informacoes(self, detalhado):

        super().exibir_informacoes(detalhado)

        print(f"Convênio: {self._nome_convenio}")
        print(f"Número da carteirinha: {self._numero_carteirinha}")