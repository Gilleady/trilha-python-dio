lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

l2 = lista.copy()
l3 = lista
l2[0] = 2
l3[0] = 3
print(lista)  # [1, "Python", [40, 30, 20]]
print(l2)  # [1, "Python", [40, 30, 20]]
print(l3)  # [1, "Python", [40, 30, 20]]