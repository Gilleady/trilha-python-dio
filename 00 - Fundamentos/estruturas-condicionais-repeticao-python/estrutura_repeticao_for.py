### FOR ... ELSE
# texto = input("Informe um texto: ")
texto = ""
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="") 
else: # Opcional e não muito comum
    print() # adiciona uma quebra de linha

# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")