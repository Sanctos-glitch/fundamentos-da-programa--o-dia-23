# As funções podem ou não receber propriedades 
def saudacao():
    print("Seja bem-vindo(a) !!!")

# saudacao()
# saudacao()
# saudacao()
# saudacao()

#Calcule o preço total de uma pizza onde será passado oum ducionário com os tamanhos e valores. Além disso, o cliente pode solicitar ou não a vorda recheada. Ao final, retorne o preço 
# 1. Pequena, Média ou Grande. Qualquer pizza terá o mesmo valor dependendo do tamanho.
# 2. Se o cliente optar dela borda recheada, deverá ser acrescido no valor da pizza + R$8.

def calcular_preco_pizza(tamanho, borda_recheada=False): 
    "Calcular o preço final de uma pizza com opções."
    tabela = {"P": 25.0, "M": 35.0, "G": 45.0}
    preco = tabela[tamanho]
    if borda_recheada == True: # O padrão é true, então tecnicamente você não precisa colocar true, pq só vi ser ture se vc falar que é false
        preco += 8.0 # preco = preco +8.0
    return preco

print(calcular_preco_pizza("P")) # 23
print(calcular_preco_pizza("P", True)) # 31
print(calcular_preco_pizza("M", False)) # 23


