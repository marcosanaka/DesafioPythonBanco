menu = """

=============== \033[1;;43m BancoPy \033[m =============== 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=========================================
=> """

#Validação do input
def verificar_numero_valido(entrada):
    # Verifica cada caractere da entrada
    for char in entrada:
        if not (char.isdigit() or char == '.'):
            return False
    
    # Tenta converter a entrada para um número de ponto flutuante
    try:
        float_value = float(entrada)
        return True
    except ValueError:
        return False

#Variaveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        entrada = input("Informe o valor do depósito: ")

        if verificar_numero_valido(entrada):

            valor = float(entrada)

            if valor > 0:
                saldo += valor
                extrato += f"\033[32mDepósito: R$ {valor:.2f}\n\033[m"

            else:
                print("\033[31mOperação falhou!\033[m O valor informado é inválido.")

        else:
            print("\033[31mOperação falhou!\033[m O valor informado é inválido.")


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\033[31mOperação falhou!\033[m Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("\033[31mOperação falhou!\033[m O valor do saque excede o limite.")

        elif excedeu_saques:
            print("\033[31mOperação falhou!\033[m Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"\033[31mSaque: R$ {valor:.2f}\n\033[m"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================\033[1;;43m EXTRATO \033[m================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n\033[1;;42m Saldo: R$ {saldo:.2f}\033[m")
        print("=========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")