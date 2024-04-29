### WHILE ... ELSE
opcao = -1

while opcao !=0:
    opcao = int(input("[1] Saca \n[2] Extrato \n[0] Sair \nEscolha uma opção: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else: # Opcional e não muito comum
    print("Obrigado por usar nosso sistema bancário, até logo!")