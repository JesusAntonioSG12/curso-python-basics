# Crearás un carrito de compras que haga las siguientes funcionalidades:
# Agregar producto
# Eliminar producto
# Mostrar la lista ordenada
# Buscar producto
# Contar productos del carrito
# Vaciar el carrito


opciones = [
    "1. Agregar producto",
    "2. Eliminar producto", 
    "3. Mostrar la lista ordenada",
    "4. Buscar producto",
    "5. Contar productos del carrito",
    "6. Vaciar el carrito",
    "7. Salir"
]

print(f"\n{"*"*40} \nCarrito de compras \nOpciones:")
for opcion in opciones:
    print(f"    {opcion}")
print(f"\n{"*"*40}\n")

shopping_cart = ['Laptop', 'Vaso', 'Cafe', "Audifonos"] # Lista inicial de productos

while True:
    option = input("Elige una opción (1-7): ")
    
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

    elif option == '7':
        print("Saliendo...")
        break

    else:
        print("Opción no válida")

        
