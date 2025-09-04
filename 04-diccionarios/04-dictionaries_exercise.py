students = {
    "Ana": [8, 7, 9],
    "Luis": [6, 5, 7],
    "Sofía": [10, 9, 10]
}

# Agregar nuevo estuadiante

students["Sergio"] = [8, 9, 10]
print(students)

# Sacar el promedio de un estudiante existente

name = "Luis"

if name in students:
    calificaciones = students[name]
    promedioExistente = sum(calificaciones)/len(calificaciones)
    print(f"El promedio de {name} es de {promedioExistente}")
else:
    print("El estudiante no existe")


# El promedio del estudiante nuevo
calificaciones = students["Sergio"]
promedioNuevo = sum(calificaciones)/len(calificaciones)

print(f"El promedio de Sergio es de {promedioNuevo}")
