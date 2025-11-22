Saldo = 2000.0
saque = float(input("Informe o valor do saque: "))
if Saldo >= saque:
    print("realizando saque")
if Saldo <= saque:
    print("Saldo insuficiente!")

Saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if Saldo >= saque:
    print("realizando saque")
else:
    print("Saldo insuficiente")


opcao = int(input("informe uma opção: [1] Sacar \n[2]Extrato: "))
if opcao == 1:
    valor = float(input("informe a quantia para saque: "))
elif opcao == 2:
    print("Exibindo o extrato... ")
else:
    print("Opção inválida")