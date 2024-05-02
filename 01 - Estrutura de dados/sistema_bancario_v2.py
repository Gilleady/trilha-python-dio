import textwrap


def menu():
    menu = """ 
    +--------- SISTEMA BANCÁRIO ---------+
    |           [d] Depositar            |
    |           [s] Sacar                |
    |           [e] Extrato              |
    |           [u] Novo Usuário         |
    |           [c] Nova Conta           |
    |           [l] Listar Contas        |
    |           [q] Sair                 |
    +------------------------------------+
    =>"""
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += "|" + f"Depósito: R$ {valor:.2f}".center(36) + "|\n"
        print("Deposito feito com sucesso")

    else:
        print("Valor inválido para depósito. Tente novamente!")

    return saldo, extrato


def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saques = numero_saques >= limite_saques
    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo

    if excedeu_saques:
        status_operacao = "Operação falhou! Número máximo de saques excedido."

    elif excedeu_limite:
        status_operacao = "Operação falhou! O valor do saque excede o limite."

    elif excedeu_saldo:
        status_operacao = "Operação falhou! Você não tem saldo suficiente."

    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += "|" + f"Saque: R$ {valor:.2f}".center(36) + "|\n"
        status_operacao = "Saque efetuado com sucesso! Verifique o extrato para mais informações."

    else:
        status_operacao ="Operação falhou! Valor informado é inválido."
    
    print(status_operacao)

    return saldo, extrato, numero_saques


def exibir_extrato(saldo,/,*,extrato):
    print("+------------- EXTRATO --------------+")
    print("| Não foram realizadas movimentações | " if not extrato else extrato.rstrip())
    print("|"+f"Saldo da conta: R$ {saldo:.2f}".center(36)+"|")
    print("+------------------------------------+")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF que deseja cadastrar (somente números):")
    usuario_filtrado = filtrar_usuario(cpf, usuarios)

    if usuario_filtrado:
        print("\nUsuário já cadastrado com CPF informado!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco (Logradouro, nº - Bairro - Cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def criar_conta(contas, agencia, usuarios):
    cpf = input("Informe o CPF do usuário (somente números):")
    usuario_filtrado = filtrar_usuario(cpf, usuarios)

    if usuario_filtrado:
        numero_conta = len(contas) + 1
        contas.append({"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario_filtrado})
        print("Conta criada com sucesso!")
    else:
        print("Usuário não encontrado, operação de criação de conta cancelada!")


def listar_contas(contas):
    linha = "+" + "-" * 36 + "+\n"
    for conta in contas:
        linha += "|" + f"Agência: {conta['agencia']}".center(36) + "|\n"
        linha += "|" + f"C/C: {conta['numero_conta']}".center(36) + "|\n"
        linha += "|" + f"Titular: {conta['usuario']['nome']}".center(36) + "|\n"
        linha += "+" + "-" * 36 + "+\n"

    print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Insira um valor para depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Insira um valor que deseja sacar: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            criar_conta(contas, AGENCIA, usuarios)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
