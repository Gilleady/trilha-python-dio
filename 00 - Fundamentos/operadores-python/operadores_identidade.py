curso = "Curso de Python"
nome_curso = curso
saldo, limite = 1000, 200

print(curso is nome_curso) # True
print(curso is not nome_curso) # False
print(saldo is limite) # False