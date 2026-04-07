print("Sistema de Empréstimo Bancário")

# Entradas dos dados
idade = int(input("Digite a idade:"))

salário = float(input("Digite o salário do cliente"))
tempo_trabalho = int(input("Digite o tempo de trabalho (em anos):"))



# Estruturas condicionais
if idade < 18:
    print("Empréstimo negado, Cliente menos de idade.")
elif salário >= 5000: 
    print("Empréstimo aprovado automaticamente.")
elif idade >= 18 and salário >= 2000 and tempo_trabalho >=2:
    print("Empréstimo aprovado.")
else: 
    print("Empréstimo negado.")
# Verifique a idade, p salario e o tempo de trabalho



