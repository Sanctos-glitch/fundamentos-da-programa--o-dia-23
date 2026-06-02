# Parâmetros nomeados - Ao nomear os argumentos, a ordem não importa mais.

def registrar_cliente(nome, telefone, endereço):
    print("=== DADOS DO CLIENTE===")
    print(" Cliente: {nome}")
    print(" Telefone: {telefone}")
    print(" Endereço: {endereço}")

    # registrar_cliente(
    #     telefone="219856484",
    #     nome="Ana Lima",
    #     endereço="Rua das pizzas, 42"
    # )

    #Retorno de valores - desempacotamento de retorno (unpacking) - Devolve uma tupla com os returns

    def resumo_pedido(itens, desconto=0):
        subtotal = sum(itens)
        valor_desconto = subtotal * (desconto / 100)
        total = subtotal - valor_desconto 
        return subtotal, valor_desconto, total # devolde uma tupla (subtotal, valor_desconto, total)
    
    #Invocando e desenpacotando a função/retorno

    sub, desc, tot = resumo_pedido([35.0, 12.0, 8.5], desconto=10)
    print(f" Subtotal: R$ {sub:.2f}")
    print(f" desconto: R$ {sub:.2f}")
    print(f" total: R$ {sub:.2f}")
