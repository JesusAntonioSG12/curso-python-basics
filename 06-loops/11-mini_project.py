inventorio = {
    "chocolate": 10, # Dulce : Precio
    "gomitas": 5,
    "paleta": 8,
    "chile": 2,
    "mexicano": 8,
    "galleta": 12
}

carito = []
precio_total = 0

cantodad_de_asteriscos = 40

print(f"\n{"*"*cantodad_de_asteriscos} \nBienvenido a la tienda, DevCandy! \n Inventario:")

for product, quantity in inventorio.items():
    print(f"- {product}: ${quantity}")

print(f"- Escribe 'salir' para terminar\n{"*"*cantodad_de_asteriscos}\n")


while True:
    opcion = input("\nElige un producto\n>").lower()

    if opcion in inventorio.keys():
        carito.append(opcion.lower())
        print(f"{opcion} agregado al carrito")

    elif opcion == 'salir':
        break

    else:
        print("Producto no identificado")

for producto in carito:
    precio_total += inventorio[producto]

print(f"Precio total a pagar: ${precio_total}")