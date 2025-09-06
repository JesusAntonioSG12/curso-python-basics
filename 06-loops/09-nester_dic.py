nested_dict = {
    "Persona1": {"Nombre": "Juan", "Edad": 30},
    "Persona2": {"Nombre": "Ana", "Edad": 25},
    "Persona3": {"Nombre": "Luis", "Edad": 35}
}

for key_1, value_1 in nested_dict.items():
    print(key_1)
    for key_2, value_2 in value_1.items():
        print(f"{key_2}: {value_2}")