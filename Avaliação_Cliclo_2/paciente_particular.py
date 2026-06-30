from paciente import Paciente
# PacienteParticular: subclasse classe filha
# Pagamento direto
# Atributo: Forma_pagamento,  desconto:fidelidade
# Método sobrescrito: exibir_informacoes()
# Método especifico: calcular_valor_final()


class PacienteParticular(Paciente):
    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario, desconto_fidelidade, forma_pagamento):

        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)

        self._forma_pagamento = forma_pagamento
        self._desconto_fidelidade = desconto_fidelidade
    
    #metodo especifico
    def calcular_valor_final(self, valor_consulta, taxa_urgencia):
        total = valor_consulta + taxa_urgencia
        desconto = valor_consulta * self._desconto_fidelidade
        valor_final = total - desconto
        return valor_final
    
    #Sobreescrita de metodo
    def exibir_informacoes(self, detalhado):
        
        super().exibir_informacoes(detalhado)


        print(f"Forma de Pagamento: {self._forma_pagamento}")
        print(f"Desconto Fidelidade: {self._desconto_fidelidade * 100:.0f}%")

