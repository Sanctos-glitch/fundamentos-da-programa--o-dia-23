while True:
    print("Sistema de controle de entrada.")
    print(" 1. Registrar minha Entrada")
    print(" 2. Ver lista de convidados ")
    print(" 3. Sair")

    opcao = input("Escolha uma opção:")

    if opcao == "1" :
        nome = input("Por favor informe o nome do visitante.")
        print(f"Entrada de {nome} registrada!")
        idade = int(input("Por favor informe idade do visitante."))
        print(f"Entrada de {idade} registrada!")
        convite = input("O visitante possui um convite? [sim ou não]")
        print(f"Entrada de {convite} regristrada!")

    elif opcao == "2" :
        print("Exibindo lista de convidados") 

    elif opcao == "3": 
            print("Sistema encerrado. Obrigado por vir!")
            break

    else:
        print("Opção invalida. Tente novamente.")

    if idade < 16 :
        print("Entrada negada. Usuario menor de idade.")

    elif convite == "não" :
        print("Entrada negada. Visitante não convidado.")
    
    else:
         print("Entrada permitida.")








