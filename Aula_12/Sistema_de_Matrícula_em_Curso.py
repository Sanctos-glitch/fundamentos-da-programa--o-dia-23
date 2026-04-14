print("Sistema de Matrícula📚")

idade= int(input("Por Favor informe sua idade."))
nota= float(input("Por Favor informe sua nota."))
frequencia= float(input("Por Favor informe sua frequência no curso.[em procentagem]"))

if idade < 18: 
    print("❌Matricula negada. Aluno menor de idade❌")

elif nota >=9:
    print("Matrícula aprovada automaticamente!✅🚀")

elif frequencia >= 75:
    print("Matrícula aprovada!✅")

if idade >= 18 and nota >= 6 and frequencia >= 75:
    print("Matrícula realizada com sucesso!")
    print("A idade informada é: {idade} anos, a nota informada é: {nota} e a frequência informada é: {frequencia}%. Matrícula realizada com sucesso!!✅🎉 ")

if idade > 18 and nota >=9:
    print("Aprovação automaticamente!✅🚀")

elif nota < 6:
    print("❌Matrícula negada. Nota insuficiente.❌")

elif frequencia <75 and nota <9 : 
    print("❌Matrícula negada. Frequência insuficiente.❌") 



