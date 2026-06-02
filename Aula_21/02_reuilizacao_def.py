def calcular_preco_pizza(tamanho):
    tabela = {"P": 25.0, "M": 35.0, "G": 45.0}
    return tabela.get(tamanho, 0)