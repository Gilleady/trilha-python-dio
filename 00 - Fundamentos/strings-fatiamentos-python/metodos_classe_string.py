### LOWER ... UPPER ... TITLE
nome = "VaRieAvEl"

print(nome.lower())
print(nome.upper())
print(nome.title())

### STRIP ... LSTRIP ... RSTRIP
texto = "   Olá Mundo!  "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

### CENTER ... JOIN
menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14,"#"))

### JOIN
print("P-y-t-h-o-n")
print("-".join(menu))