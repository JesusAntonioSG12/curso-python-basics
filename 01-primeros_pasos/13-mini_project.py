# REGISTRO
# Recibe de forma dinámica el nombre, el año de nacimiento, correo y contraseña

"""
Nombre: x
Email: x
Tendrás x en el año 2050
Tu contraseña es: ********
"""

name = input("Ingresa tu nombre: ")
email = input("Ingresa tu correo electronico: ")
birth_year = input("Ingresa tu año de nacimiento: ")
password = input("Ingresa una contraseña: ")

new_age = 2050 - int(birth_year)
password_length = len(password)



print(f"""
      Nombre: {name}
      Email: {email}
      Tendrás {new_age} en el año 2050
      Tu contraseña es: {'*' * password_length}
      """)
