# for index, char in enumerate('Devtalles'):
#     print(index, char)

# for index, number in enumerate([1, 2, 3, 4, 5]):
#     print(index, number)


for index, number in enumerate(list(range(100))):
    if number % 2 == 0:
        print("Es un numero par:", number)
    else:
        print("Es un numero impar:", number)
