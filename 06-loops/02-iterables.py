
numbers = [1, 2, 3, 4, 5]
# Iterables: Iterables, listas, diccionarios, set, tuplas
# Iterador: Objeto que recuerda su posicion

# for number in numbers:
#     print(number)

iterator = iter(numbers)

# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

user = {
    'name': 'Sergio',
    'age': 25,
    'can_swim': True
}

for item in user.items():
    key, value = item
    print(f"{key}: {value}")
