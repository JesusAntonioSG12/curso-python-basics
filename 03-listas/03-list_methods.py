# shopping_cart = [
#     "Camisas", "Tenis", "Calcetas", "Pantalones"
# ]

# # Insertar
# print("INSERTAR")

# shopping_cart.append("Gorras")
# print("Append", shopping_cart)

# shopping_cart.insert(0, "Lentes")
# print("Insert", shopping_cart)

# shopping_cart.extend(["Mochila", "Calzones"])
# print("Extend", shopping_cart)

# # Eliminar
# shopping_cart = [
#     "Camisas", "Tenis", "Calcetas", "Pantalones"
# ]

# print("ELIMINAR")


# shopping_cart.pop()
# print("Pop sin index", shopping_cart)
# shopping_cart.pop(1)
# print("Pop con index", shopping_cart)

# shopping_cart.remove("Pantalones")
# print("Remove", shopping_cart)

# shopping_cart.clear()
# print("Clear", shopping_cart)

# # Buscar
# shopping_cart = [
#     "Camisas", "Tenis", "Calcetas", "Pantalones"
# ]

# print("BUSCAR")

# print(shopping_cart.index("Tenis", 0, 4))
# print("Calcetas" in shopping_cart)

# # CONTAR
# print(shopping_cart.count("Pantalones"))

# ORDENAMIENTO
shopping_cart = [
    "Camisas", "Tenis", "Calcetas", "Gorra", "Pantalones"
]

shopping_cart.sort()
print(shopping_cart)

new_shopping_cart = sorted(shopping_cart)
print(new_shopping_cart)

other_shopping_cart = shopping_cart.copy()

final_shopping_cart = shopping_cart.reverse()