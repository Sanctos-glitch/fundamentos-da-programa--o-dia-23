print("Sistema de controle de estacionamento")

idade= int(input("Por Favor informe sua idade."))
cadastro= (input("O(a) senhor (a) possui cadastro no shopping? "))
veiculo= (input("Por favor informe o tipo do seu veículo.[pequeno],[médio],[longo]" ))
vip= (input("O(a) senhor(a) é um(a) cliente vip?"))

if idade < 18:
    print("Entrada negada automaticamente. Cliente menor de idade.")

elif vip == "sim" and idade < 18: 
    print("Aprovação automatica! Bem vindo cliente vip.")

elif vip == "não":
    print("Cliente não vip.")

if cadastro == "sim" and idade <= 18 and vip == "não":
    print("Entrada aprovada! Bem vindo parceiro!")

elif veiculo == "longo" and cadastro == "sim":
    print("Entrada negada automaticamente. Veiculo grande de mais.")

if idade >= 18 and cadastro == "sim" and veiculo == "pequeno" or veiculo == "médio" and vip == "não":
    print("A idade informada foi: {idade} anos, o cliente é cadastrado? {cadastro} e o tamanho do veiculo é: {veiculo}. Entrada aprovada! aproveite a visita.")

