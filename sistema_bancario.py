saldo = 0
limite = 500
extrato = " "
num_saques = 0
LIMITE_SAQUES = 3

while True: #ciclo infinito

    opcao = int(input("Digite a opção que deseja: \n [1] Depósito \n [2] Saque \n [3] Extrato \n [4] Sair \n"))

    if opcao == 1:
        x = "DEPÓSITO"
        y = ""
        print(x.center(40, "-"))
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} \n"

            print(y.center(40, "-"))

        else:
            print("Informe um valor válido!")
            print(y.center(40, "-"))

    elif opcao == 2:
        x = "SAQUE"
        y = ""
        print(x.center(40, "-"))
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = num_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou! O saldo de sua conta bancária é insuficiente para o saque!")
            print(y.center(40, "-"))

        elif excedeu_limite:
            print("Operação falhou! O saque pedido é maior que o limite (R$ 500.00)")
            print(y.center(40, "-"))

        elif excedeu_saques:
            print("Operação falhou! Número de saques diários atingidos!")
            print(y.center(40, "-"))

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            num_saques == 1
            print(y.center(40, "-"))

        else:
            print("Operação falhou! O valor informado é inválido!")
            print(y.center(40, "-"))

    elif opcao == 3:
        x = "EXTRATO"
        y = ""
        print(x.center(40, "-"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(y.center(40, "-"))

    elif opcao == 4:
        print("Saindo...")
        break

    else:
        print("Opção inválida! Digite um dos quatro números que está na lista!")

