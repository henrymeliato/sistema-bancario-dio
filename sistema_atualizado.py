def menu():
    x_menu = "MENU"
    print(x_menu.center(60, "="))
    opcao_menu = int(input("""DIGITE A OPÇÃO QUE DESEJA:
[1] Depósito
[2] Sacar
[3] Extrato
[4] Nova Conta
[5] Listar Contas
[6] Novo Usuário
[7] Sair
"""))
    return opcao_menu

def deposito(saldo, valor, /, extrato):

    x = "DEPÓSITO"
    print(x.center(60, "-"))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} \n"
        print("Depósito realizado!")
        

    else:
        print("Informe um valor válido!")
        

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, num_saques, limite_saques):
    x = "SAQUE"
    print(x.center(60, "-"))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = num_saques >= limite_saques

    if excedeu_saldo:
        print("Operação Falhou! O saldo de sua conta bancária é insuficiente para o saque!")
        

    elif excedeu_limite:
        print("Operação falhou! O saque pedido é maior que o limite (R$ 500.00)")
        

    elif excedeu_saques:
        print("Operação falhou! Número de saques diários atingidos!")
        

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        num_saques += 1
        print("Saque realizado!")
        

    else:
        print("Operação falhou! O valor informado é inválido!")
        

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    x = "EXIBIÇÃO DO EXTRATO"
    print(x.center(60, "-"))
    
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    
def criar_usuario(usuarios):
    x = "USUÁRIO"
    print(x.center(60, "-"))

    cpf = input("DIGITE SEU CPF (apenas números): ")
    usuarios = listar_usuario(cpf, usuarios)

    if usuarios:
        print("Este usuário já existe!")
        return
    
    nome = input("DIGITE SEU NOME COMPLETO: ")
    data_nas = input("DIGITE SUA DATA DE NASCIMENTO: ")
    endereco = input("DIGITE SEU ENDEREÇO (logradouro, numero - bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "data_nas": data_nas, "endereco": endereco})

    print("USUÁRIO CRIADO!")
    
def listar_usuario(cpf, usuarios):
    x = "LISTAR USUÁRIOS"
    print(x.center(60, "="))
    usuarios_listados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_listados[0] if usuarios_listados else None
    
def criar_conta(agencia, numero_conta, usuarios):
    x = "NOVA CONTA"
    print(x.center(60, "="))
    cpf = input("DIGITE O CPF DO USUÁRIO: ")
    usuario = listar_usuario(cpf, usuarios)

    if usuario:
        print("CONTA CRIADA!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuarios": usuarios}
    
    print("USUÁRIO NÃO ENCONTRADO")
    
def main():

    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True: #ciclo infinito
        opcao = menu()

        if opcao == 1:
            valor = float(input("Digite o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato=extrato)

        elif opcao == 2:
            valor = float(input("Digite o valor que deseja sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            numero_conta =len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 5:
            listar_usuario(contas)

        elif opcao == 6:
            x = "NOVO USUÁRIO"
            print(x.center(60, "-"))
            criar_usuario(usuarios)

        elif opcao == 7:
            print("Saindo...")
            break

        else:
            print("Opção inválida! Digite um dos quatro números que está na lista!")

main()


