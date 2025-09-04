# Instrucciones:
# Crearás un programa de evaluación de candidatos potenciales con conocimientos en Python para RH.
# Obtendrás el nombre, años de experiencia y habilidades.

# Evaluarás:
# * Si el candidato sabe Python/Django, tiene +3 años de experiencia: Candidato Optimo
# * Si el candidato sabe Python/Django, tiene +1 año de experiencia: Buen candidato
# * Si el candidato sabe Python/Django: Posible candidato
# * Si el candidato no sabe Python: No optimo, se guardará CV

# ? Consejo: Ocupa los metodos .split()

nombre = input("Nombre del candidato: ")
experiencia = int(input("Ingresa tus años de experiencia: "))
conocimientos = input(
    "Ingresa las tecnologías que dominas: ").upper().split(",")

tieneHabilidades = "PYTHON" in conocimientos or "DJANGO" in conocimientos

if tieneHabilidades:
    if experiencia >= 3:
        print(f"{nombre} es un candidato optimo")
    elif experiencia >= 1:
        print(f"{nombre}es un buen candidato")
    else:
        print(f"{nombre} es un posible candidato")
else:
    print(f"{nombre} no es optimo, se guardará CV")
