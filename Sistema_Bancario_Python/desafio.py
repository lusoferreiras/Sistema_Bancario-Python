menu = """
    
    Digita a opção que deseja realizar:
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print("\nBem vindo ao nosso sistema bancário!")

while True:
    opcao = input(menu)
    if opcao == "d":
        print("Depósito\n")
        valor = float(input("Insira o valor de deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else: 
            print("\nOperação falhou!\nO valor informado é inválido.") 

    elif opcao == "s":
        print("Saque\n")

        valor = float(input("Informe o valor que deseja realizar o saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOperação falhou!\nVocÊ não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("\nOperação falhou!\nO valor do saque excede o limite.\n**  500 reais por saque  **")

        elif excedeu_saques:
            print("\nOperação falhou! Número de saques excedido.\n**  3 saques diários  **")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falou!\nO valor informado é inválido.")            
    elif opcao == "e":
        print("Extrato")
        print("\n================= EXTRATO ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================================")

    elif opcao == "q":
        print("Obrigado. Até a próxima!")
        break

    else:
        print("Operação inválido, por favor selecione novamente a operação desejada.")

            

