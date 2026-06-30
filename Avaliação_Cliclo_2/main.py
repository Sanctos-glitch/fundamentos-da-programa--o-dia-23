from paciente_particular import PacienteParticular
from paciente_convenio import PacienteConvenio

print("=== INICIANDO SISTEMA DA CLÍNICA MÉDICA ===\n")

paciente_particular = PacienteParticular(
    "Dean Winchester", "24/01/1979", "079.112.196-67",
    "(11) 86690-3235", "O+", "PRONT-001",
    "Pix", 0.10

)


paciente_convenio = PacienteConvenio(
    "Ana Maria Silva", "25/08/1985", "987.654.321-11", 
    "(21) 97777-6666", "A-", "PRONT-002", 
    "Plano de Saúde", "111222333444555"
)


print("Paciente particular")

paciente_particular.exibir_informacoes(detalhado=True)


valor_final = paciente_particular.calcular_valor_final(valor_consulta=200.00, taxa_urgencia=50.00 )
print(f"Valor Final da Colsulta: R$ {valor_final:.2f}\n")


print("paciente por convênio ")

paciente_convenio.exibir_informacoes(detalhado=False)

print()
paciente_convenio.registrar_autorizacao(procedimento="Exame de Sangue", valor_recusado=0.00)

print("\n=== FIM DOS TESTES ===")


