# Crearás un carrito de compras que haga las siguientes funcionalidades:
# Agregar producto
# Eliminar producto
# Mostrar la lista ordenada
# Buscar producto
# Contar productos del carrito
# Vaciar el carrito

print("Carrito de compras")
print("Opciones: ")
print("1. Agregar producto")
print("2. Eliminar producto")
print("3. Mostrar la lista ordenada")
print("4. Buscar producto")
print("5. Contar productos del carrito")
print("6. Vaciar el carrito")

shopping_cart = ['Laptop', 'Vaso', 'Cafe', "Audifonos"]
option = input("Elige una opción (1-6): ")

if option == '1':
    new_product = input("Ingresa el nombre del producto: ")
    if new_product not in shopping_cart:
        shopping_cart.append(new_product)
        print("Producto agregado")
    else:
        print("El producto ya se encuentra en la lista")

elif option == '2':
    delete_product = input("Ingrese el nombre del producto a eliminar: ")

    if delete_product in shopping_cart:
        shopping_cart.remove(delete_product)
        print("Producto eliminado")
    else:
        print("Producto no encontrado")

elif option == '3':
    if len(shopping_cart) > 0:
        shopping_cart.sort()
        print(shopping_cart)
    else:
        print("No es posible ordenar. La lista esta vacía")

elif option == '4':
    find_product = input("Ingrese el nombre del producto a buscar: ")

    if find_product in shopping_cart:
        print(f"{find_product} encontrado en la lista")
    else:
        print("Producto no encontrado")

elif option == '5':
    print(len(shopping_cart))
elif option == '6':
    shopping_cart.clear()
    print("Lista vacía")
else:
    print("Opción no válida")
