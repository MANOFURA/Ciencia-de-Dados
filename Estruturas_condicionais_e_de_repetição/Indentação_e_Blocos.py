def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!", saldo)
        print("retire o seu dinheiro na boca do caixa")

    else:
        print("Saldo insuficiente")
        print("Obrigado e tenha um ótimo dia!")

sacar(1000)