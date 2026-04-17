total_gasto = 0
quantidade_de_produtos = 0

while True:
    print("Sistema de Caixa de Supermercado")
    valor = float(input("Digite o valor do produto (ou 0 para encerrar)"))

    if valor == 0:
        break

    total_gasto += valor
    quantidade_de_produtos += 1
    
    print(f"Produtos de R${valor:.2f} adicionado!")
    
if quantidade_de_produtos > 0:
    media = total_gasto / quantidade_de_produtos
   
    print("Resumo da compra")
    print(f"Total da compra : R${total_gasto:2f}")
    print(f"Quantidade de produtos: {quantidade_de_produtos}")
    print(f"Média de valores: R${media:.2f}")

else: 
    print("Nenhum produto foi registrado.")




   

