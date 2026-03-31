# Variáveis da pizzaria
FRETE = 2 #Constante Fake em python
pizza_sabor = input("Informe o sabor da pizza: [frango com requeijão], [calabresa], [mussaela], [banana com chocolate]: ") 
pizza_tamanho = input ("Informe o tamanho da pizza: [pequena], [média], [grande]: ")
dia_semana = input("Informe o dia da semana: [quarta], [quinta], [sexta], [sábado], [domingo]: ")

print(f" O sabor escolhido da pizza é {pizza_sabor}, o tamanho é {pizza_tamanho}, e hoje é {dia_semana}.")
# promoções -> estruturas condicionais 

# Comprando qualquer pizza qualquer tamanho no sábado, o refri é gratúito
if dia_semana == "sabado":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"🥤O Refri hoje é porconta da casa.")
elif dia_semana == "domingo": 
    print(f"🍕Pedido aceito com sucesso!")
    print(f"🥤O Frete e o Refri hoje é porconta da casa.")
elif pizza_sabor == "calabresa" and pizza_tamanho == "média":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"🥤O Frete e o Refri hoje é porconta da casa.")

#comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são gratúitos

