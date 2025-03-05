saq_diario = 0
saldo = 0
LIMITE = 500
LIMITE_SAQUE = 3
extrato = ""

menu = """
[1] Depositar
[2] Sacar
[3] Extrato 
[4] Sair

Escolha uma opção: """

def deposito():
    global saldo, extrato
    try:
        valor = float(input("Digite o valor de depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: +R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Erro: O valor do depósito deve ser maior que zero.")
    
    except ValueError:
        print("Erro: Digite um valor numérico válido.")

def saque():
    global saq_diario, saldo, extrato

    if saq_diario < LIMITE_SAQUE:  
        try:
            valor = float(input("Digite o valor de saque: "))

            if valor > saldo:
                print("Erro: Saldo insuficiente!")

            elif valor > LIMITE:
                print("Erro: O limite máximo por saque é de R$ 500.")

            elif valor <= 0:
                print("Erro: O valor do saque deve ser maior que zero.")

            else:
                saldo -= valor
                saq_diario += 1
                extrato += f"Saque: -R$ {valor:.2f}\n"
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

    else:
        print("Erro: Você atingiu o limite de 3 saques diários.")

def extratos():
    global extrato
    print("\n=== EXTRATO BANCÁRIO ===")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("========================\n")

# Loop do menu principal
while True:
    try:
        opcao = int(input(menu))

        if opcao == 1:
            deposito()
        
        elif opcao == 2:
            saque()
        
        elif opcao == 3:
            extratos()
        
        elif opcao == 4:
            print("Saindo do sistema... Obrigado!")
            break
        
        else:
            print("Erro: Opção inválida! Tente novamente.")

    except ValueError:
        print("Erro: Digite um número válido.")
