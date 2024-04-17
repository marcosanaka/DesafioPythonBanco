import textwrap

def menu():
    """Função para exibir o Menu"""
    menu = """\n
    =============== \033[1;;43m BancoPy \033[m ===============
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [9]\tSair
    =========================================
    => """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    """Função para depositar um valor na conta"""
    if valor > 0:
            saldo += valor
            valor_extrato = f'{valor:.2f}'
            extrato += (f"\033[32mDepósito: R$ {valor_extrato.replace('.',',')}\n\033[m")

    else:
        print("\033[31mOperação falhou!\033[m O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, limite_saque):
    """Função para sacar um valor da conta"""
    
    if limite_saque > 0:
    
        excedeu_saldo = valor > saldo
    
        excedeu_limite = valor > limite

    
        if excedeu_saldo:
            print("\033[31mOperação falhou!\033[m Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("\033[31mOperação falhou!\033[m O valor do saque excede o limite.")
        
        elif valor > 0:
            saldo -= valor
            saque_extrato = f'{valor:.2f}'
            extrato += (f"\033[31mSaque: R$ {saque_extrato.replace('.',',')}\n\033[m")
            limite_saque -= 1

        else:
            print("\033[31mOperação falhou!\033[m O valor informado é inválido.")

    else:

        print("\033[31mOperação falhou!\033[m Número máximo de saques excedido.")

    return saldo, extrato, limite_saque

def exibir_extrato(saldo, /, *, extrato):
    """Função para acessar o extrato da conta"""
    saldo_extrato = f'{saldo:.2f}'
        
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n\033[32mSaldo: R$ {saldo_extrato.replace('.',',')}\033[m1")
    print("==========================================")

def cadastrar_usuario(usuarios):
    """Função para cadastrar novos usuários"""
    cpf = input("\nDigite o seu CPF: ")
    cpf = cpf_formatado(cpf)

    if cpf.isalnum() and len(cpf) == 11:
        
        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
                print (f"""\033[31mJa existe usuario cadastrado com o CPF! {cpf[:3]}.
                    {cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}\033[m""")

        else:
            nome = input("\nDigite o seu nome: ")
            data_nascimento = input("\nDigite sua data de nascimento: ")
            estado = input("\nDigite o nome do seu estado: ")
            cidade = input("\nDigite o nome da sua cidade: ")
            rua = input("\nDigite o logradouro da sua rua: ")
            numero_casa = input("\nNumero da sua residencia: ")
            bairro = input("\nDigite o nome do seu bairro: ")
            
            endereco = (f"{rua}, {numero_casa} - {bairro} - {cidade}/{estado}")
            
            usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
            
            print("\033[32m=== Usuário criado com sucesso! ===\033[m")

    else:

        print("\033[31mNumero de CPF invalido!\033[m")
    
def filtrar_usuario(cpf, usuarios):
    """Função para verificar se existem usuarios já cadastrados com o mesmo CPF"""
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cpf_formatado(cpf):
    """Função para formatar o CPF sem pontos ou tracos Ex: 12345678912 """
    cpf = cpf.strip()
    cpf = cpf.replace('.','').replace('-','')
    return cpf
   
def cadastrar_conta(agencia, numero_conta, usuarios):
    """Função para cadastrar novas contas"""
    cpf = input("Informe o CPF do usuário: ")
    cpf = cpf_formatado(cpf)
    
    if cpf.isalnum() and len(cpf) == 11:
        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
            print("\n\033[32m=== Conta criada com sucesso! ===\033[m")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}


    print("\n\033[31m Usuário não encontrado, fluxo de criação de conta encerrado!\033[m ")

def listar_contas(contas):
    """Função para listar as contas cadastradas"""
    if contas:
        for conta in contas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(linha)
    else:
        print("\nAinda não existem contas cadastradas.")

def main():
    """Função para inicio do programa"""

    saldo = 0
    AGENCIA = "0001"
    LIMITE = 500
    extrato = ""
    limite_saque = 3
    usuarios = []
    contas = []
    
    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        

        elif opcao == "2":
            
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, limite_saque = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=LIMITE,
            limite_saque=limite_saque,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            cadastrar_usuario(usuarios)

        elif opcao == "9":
            break
    
        else:
            print("\033[31mOperação inválida,\033[m1 por favor selecione novamente a operação desejada.")

main()