
idade = int(input("Informe sua idade"))
salario = float(input("Informe seu salário"))
tempo_de_trabalho = int(input ("Informe o seu tempo de trabalho [em anos]"))
emprestimo = float(input("Informe o valor do seu empréstimo" ))
parcelas = int(input("Em quantas parcelas deseja pagar? "))
valor_parcela = emprestimo/parcelas
limite_parcela = salario*0.3
  


if idade < 18:
    print("Empréstimo negado")
elif salario >= 5000:
    print("aprovação Automática!")
if salario >= 2000:
    print("aprovado!")
elif salario >= 2000 and tempo_de_trabalho >= 2: 
    print(" aprovado!")
    print('A idade informada é {idade} anos, o salário informado é {salario} reais e o tempo de trabalho informado é {tempo_de_trabalho} anos. Empréstimo realizado com exito!👍')

if salario >= 5000 and valor_parcela <= limite_parcela:
    print("Aprovação Automática!")
        
elif salario >= 2000 and tempo_de_trabalho >= 2 and valor_parcela <= limite_parcela:
    print("Empréstimo Aprovado! 👍")
        
elif valor_parcela > limite_parcela:
    print("Empréstimo Negado: O valor da parcela compromete muito o seu salário.")
    
else:
    print("Empréstimo Negado, requisitos de tempo de serviço ou renda não atingidos.")
 
    





