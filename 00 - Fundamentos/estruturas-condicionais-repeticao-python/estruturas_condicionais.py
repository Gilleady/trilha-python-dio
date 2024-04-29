### IF .. ELIF .. ELSE 
MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua diade: "))
# 1º forma
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

# 2º forma (mais eficiente)
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")

# 3º forma (elif)
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode faze aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")
