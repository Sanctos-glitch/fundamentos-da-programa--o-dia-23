# Crie um sistema aonde o valor unicial é de R$1000 e o usuario consiga realizar um saue e ao final sera exibido o valos restante do saldo.
saldo = 1000
while saldo > 0:
    saque = float(input("digite o valor do saque:"))
    saldo -= saque  # saldo = saldo - saque 
    print(f'saldo restante: {saldo}')
