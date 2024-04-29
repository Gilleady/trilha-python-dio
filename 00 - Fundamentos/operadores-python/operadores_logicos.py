saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite) # False
print(saldo >= saque or saque <= limite) # True

print(not 1000 > 1500) # True

contatos_emergencia = []
print(not contatos_emergencia) # True

print(not "saque 1500;") # False

print(not "") # True

saldo = 1000
saque = 200
limite = 100
conta_especial = True

expressao_1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expressao_1) # True

expressao_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao_2) # True

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque
expressao_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(expressao_3) # True