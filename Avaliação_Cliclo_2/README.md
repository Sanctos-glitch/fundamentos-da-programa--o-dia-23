# Sistema de Gestão de Clínica Médica

Este projeto é um sistema de gerenciamento de pacientes para uma clínica médica, desenvolvido em Python utilizando os pilares da Programação Orientada a Objetos (POO), como herança, encapsulamento e polimorfismo.

##  Estrutura do Projeto

O sistema é dividido em três classes principais, organizadas em arquivos separados:

1. **Paciente (`paciente.py`):** Superclasse que armazena os dados comuns de todos os pacientes.
   * *Métodos:* `registrar_atendimento()` e `exibir_informacoes()`.
2. **PacienteParticular (`paciente_particular.py`):** Subclasse para pacientes com pagamento direto.
   * *Métodos:* `calcular_valor_final()` e a sobrescrita de `exibir_informacoes()`.
3. **PacienteConvenio (`paciente_convenio.py`):** Subclasse para pacientes atendidos via plano de saúde.
   * *Métodos:* `registrar_autorizacao()` e a sobrescrita de `exibir_informacoes()`.

## 🚀 Como Executar e Testar

Para rodar os testes do sistema e verificar o funcionamento das classes, execute o arquivo principal no seu terminal:

```bash
python main.py
```

## 👤 Aluno
* **Nome Completo:** [Mariana Ferreira Santos]
