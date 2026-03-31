# Estrutura de repetição
# if (se) -> Verifica se o uma condição é true (versadeira). Se for, ele executa o cídogo.
# elif (senão se) -> é usado para testar várias condições. Ele só executa se todas as condições anteriores foram falsas.
# else (senão) -> executa o código se a condição for false (falsa).

# idade_usuario = 15
# # if o usuário for maior de 18 anos,eu vou passar a informação:Você é maior de idade, senão Você é menor de idade.
# if idade_usuario >= 18: 
#     print("Você é maior de idade.")
# else:
#     print("Você é menor de idade")

idade = 10
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 0 and idade < 18: 
    print("Você é jovem de idade.")
elif idade >= 70:
    print("Você é experiente de idade.")
else:
    print("Você é  menos de idade.")

