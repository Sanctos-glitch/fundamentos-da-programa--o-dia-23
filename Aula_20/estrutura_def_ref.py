def exibir_cardapio():
    print("=== CARDÁPIO PIZZARIA DO CÓDIGO ===")
    print("🍕 Margherita  - P: R$25 | M: R$35 | G: R$45")
    print("🍕 calabresa  - P: R$28 | M: R$38 | G: R$48")
    print("🍕 Frango  - P: R$30 | M: R$40 | G: R$50")

# exibir_cardapio()

# Função para aplicar desconto, onde o preço e por percentual de desconto sera passado no momento da invocação da samara.
valor_sem_desc = 40

def aplicar_desconto(preco, percentual):
    # preco * (1 - percentual /100)
    return preco * percentual

preco_final = valor_sem_desc - aplicar_desconto(valor_sem_desc, 0.10)
print(f"preço com desconto: R$ {preco_final:.2f}")

# Declarar função que receberá por padrão que a borda não pé recheada. Além disso, trá receber também  o sabor e tamanho da pizza. 
def fazer_pedido(sabor, tamanho= "M", borda_recheada=False):
    borda = "Com borda recheada" if borda_recheada else "sem borda"
    # variavel = valor se verdadeiro if condição Lógica else valor se  falso.
    print(f'Pedido: {sabor} | {tamanho} | {borda}')

fazer_pedido("Margherita")
fazer_pedido("Frango", "G")
fazer_pedido("Calabresa", "P", True)







 